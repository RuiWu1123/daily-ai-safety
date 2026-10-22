// usage: NODE_PATH=/opt/node22/lib/node_modules node tools/fetch_texts.js <items.json> <textsdir>
// items.json: [{id,url,title,date}], writes <textsdir>/<id>.txt (main innerText + useful links). Skips existing files >2000 bytes.
const { chromium } = require('playwright');
const fs=require('fs');
const [itemsFile,dir]=process.argv.slice(2);
fs.mkdirSync(dir,{recursive:true});
const items=JSON.parse(fs.readFileSync(itemsFile));
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'});
  const queue=[...items];
  async function worker(){
    const p=await ctx.newPage();
    while(queue.length){
      const it=queue.shift(); const f=`${dir}/${it.id}.txt`;
      if(fs.existsSync(f) && fs.statSync(f).size>2000) continue;
      try{
        await p.goto(it.url,{waitUntil:'domcontentloaded',timeout:60000});
        await p.waitForTimeout(3000);
        const t=await p.evaluate(()=>{const m=document.querySelector('main')||document.querySelector('article')||document.body;return m.innerText;});
        const links=await p.$$eval('a',as=>as.map(a=>a.href).filter(h=>/arxiv\.org\/(abs|pdf)|\.pdf($|\?)|openreview|github\.com/.test(h)));
        fs.writeFileSync(f,`URL: ${it.url}\nTITLE: ${it.title}\nLISTDATE: ${it.date||''}\nLINKS: ${[...new Set(links)].slice(0,12).join(' ')}\n\n`+t);
        console.log(it.id,t.length);
      }catch(e){console.log(it.id,'ERR',e.message.slice(0,80));}
    }
  }
  await Promise.all([1,2,3].map(worker));
  await b.close();
})();
