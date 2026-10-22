// Detect new posts on every monitored source.
//
// usage (from repo root):
//   NODE_PATH=/opt/node22/lib/node_modules node tools/monitor.js          -> writes tools/out/new_candidates.json
//   NODE_PATH=/opt/node22/lib/node_modules node tools/monitor.js --seed   -> adds everything currently listed to tools/seen_urls.txt
//   node tools/monitor.js --mark-seen                                      -> appends tools/out/new_candidates.json urls to seen_urls.txt
//
// A "candidate" is a URL listed by a source that is not yet in tools/seen_urls.txt.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const SEEN = path.join(__dirname, 'seen_urls.txt');
const OUT_DIR = path.join(__dirname, 'out');
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36';

function norm(u) {
  try {
    const x = new URL(u);
    x.hash = ''; x.search = '';
    let h = x.hostname.replace(/^www\.far\.ai$/, 'far.ai').replace(/goodfire\.ai$/, 'goodfire.com');
    let p = x.pathname.replace(/\/index\.html$/, '').replace(/\/+$/, '');
    return `https://${h}${p}`;
  } catch (e) { return u; }
}
function loadSeen() {
  return new Set(fs.existsSync(SEEN) ? fs.readFileSync(SEEN, 'utf8').split('\n').filter(Boolean) : []);
}
function saveSeen(set) {
  fs.writeFileSync(SEEN, [...set].sort().join('\n') + '\n');
}
function curl(args) {
  return execFileSync('curl', ['-sL', '--max-time', '60', '-A', UA, ...args], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
}

async function pageLinks(browser, src) {
  const p = await browser.newPage({ userAgent: UA });
  try {
    await p.goto(src.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await p.waitForTimeout(4000);
    for (let i = 0; i < 30; i++) {
      await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await p.waitForTimeout(600);
      const btn = p.locator('button:text-matches("(load|show|see|view) more","i")');
      if (await btn.count() === 0) { if (i > 3) break; continue; }
      try { await btn.first().click({ timeout: 3000 }); await p.waitForTimeout(1500); } catch (e) { break; }
    }
    const links = await p.$$eval('a', as => as.map(a => [(a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 300), a.href]));
    const inc = new RegExp(src.include), exc = src.exclude ? new RegExp(src.exclude) : null;
    const out = new Map();
    for (const [t, h] of links) {
      if (!inc.test(h) || (exc && exc.test(norm(h)))) continue;
      const n = norm(h);
      if (n === norm(src.url)) continue;
      if (!out.has(n) || (t && t.length > (out.get(n).text || '').length)) out.set(n, { url: n, text: t });
    }
    return [...out.values()];
  } finally { await p.close(); }
}

function rssLinks(src) {
  const s = curl([src.url]);
  return [...s.matchAll(/<item>([\s\S]*?)<\/item>/g)].map(m => {
    const it = m[1];
    const g = re => (it.match(re) || [, ''])[1].replace(/<!\[CDATA\[|\]\]>/g, '').trim();
    return { url: norm(g(/<link>([\s\S]*?)<\/link>/)), text: g(/<title>([\s\S]*?)<\/title>/), date: g(/<pubDate>([\s\S]*?)<\/pubDate>/), category: g(/<category[^>]*>([\s\S]*?)<\/category>/) };
  });
}

function substackLinks(src) {
  const out = [];
  for (let off = 0; off < 100; off += 25) {
    const s = curl([`${src.url}/api/v1/archive?sort=new&offset=${off}&limit=25`]);
    let arr; try { arr = JSON.parse(s); } catch (e) { break; }
    if (!arr.length) break;
    for (const p of arr) out.push({ url: norm(p.canonical_url || `${src.url}/p/${p.slug}`), text: p.title, date: p.post_date });
    if (off === 0 && arr.length < 25) break;
  }
  return out;
}

function afLinks(src, sinceIso) {
  const q = { query: 'query($t:JSON){ posts(input:{terms:$t}){ results { _id title postedAt pageUrl user{displayName} coauthors{displayName} } } }',
    variables: { t: { view: 'new', af: true, limit: 100, after: sinceIso } } };
  const s = curl(['-X', 'POST', src.url, '-H', 'Content-Type: application/json', '-d', JSON.stringify(q)]);
  const res = JSON.parse(s).data.posts.results;
  return res.map(p => ({ url: norm(p.pageUrl), text: p.title, date: p.postedAt, authors: [p.user && p.user.displayName, ...(p.coauthors || []).map(c => c.displayName)].filter(Boolean).join(', '), af_id: p._id }));
}

(async () => {
  const mode = process.argv[2] || '';
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const seen = loadSeen();
  if (mode === '--mark-seen') {
    const c = JSON.parse(fs.readFileSync(path.join(OUT_DIR, 'new_candidates.json')));
    for (const x of c.candidates) seen.add(x.url);
    saveSeen(seen); console.log('marked', c.candidates.length, 'seen ->', seen.size); return;
  }
  const sources = JSON.parse(fs.readFileSync(path.join(__dirname, 'sources.json')));
  const since = new Date(Date.now() - 10 * 86400e3).toISOString();
  const { chromium } = require('playwright');
  const browser = await chromium.launch();
  const candidates = [], errors = [], counts = {};
  const local = new Set();
  for (const src of sources) {
    let items = [];
    try {
      if (src.kind === 'page') items = await pageLinks(browser, src);
      else if (src.kind === 'rss') items = rssLinks(src);
      else if (src.kind === 'substack') items = substackLinks(src);
      else if (src.kind === 'af') items = afLinks(src, since);
    } catch (e) { errors.push({ source: src.url, error: String(e).slice(0, 200) }); }
    counts[src.url] = items.length;
    if (!items.length) errors.push({ source: src.url, error: 'no links found (page layout changed or fetch failed?)' });
    for (const it of items) {
      if (mode === '--seed') { seen.add(it.url); continue; }
      if (seen.has(it.url) || local.has(it.url)) continue;
      local.add(it.url);
      candidates.push({ ...it, lab: src.lab, file: src.file, section: src.section || null, research_source: src.research_source, news_filter: src.news_filter || null, listed_on: src.url });
    }
  }
  await browser.close();
  if (mode === '--seed') { saveSeen(seen); console.log('seeded', seen.size); }
  else {
    fs.writeFileSync(path.join(OUT_DIR, 'new_candidates.json'), JSON.stringify({ generated: new Date().toISOString(), counts, errors, candidates }, null, 1));
    console.log(`candidates: ${candidates.length}, errors: ${errors.length}`);
    for (const c of candidates) console.log(`- [${c.lab}] ${c.text.slice(0, 100)} | ${c.url}`);
    for (const e of errors) console.log(`! ${e.source}: ${e.error}`);
  }
})();
