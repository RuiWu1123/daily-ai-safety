# 每日更新任务说明

这份文件是定时任务每天执行的操作手册。定时任务每天美东时间早上 8 点左右运行一次，做两件事：

1. 检查所有已收录的 lab / 论坛有没有新内容（包括新闻、政策、组织动态这类非 technical research 的更新），写一份综合日报。
2. 如果新内容里有符合收录规则的 technical research，就在 `papers/<lab>/` 下为它新建一篇笔记（一篇论文一个文件），并写一段简读。

仓库是用户的 Obsidian 笔记库，用户会在电脑和 iPhone 上同时阅读、书写，所以必须遵守：

- **只新建，不修改**：每日任务只新建笔记和日报文件，绝不修改已有的论文笔记，也绝不碰 `my_notes/` 文件夹（那是用户自己写的笔记，会引用论文笔记，所以论文笔记的文件名一旦建好就不要改）。
- `index/` 下的页面是 Dataview 自动查询，新笔记会自动出现，不需要改。
- 不要提交 `.obsidian/` 下的工作区文件。

## 0. 准备

- 仓库位置：`/home/user/daily-ai-safety`。如果不存在，就 clone `https://github.com/ruiwu1123/daily-ai-safety`（如果 git 没有权限，先用 `add_repo` 工具加 `ruiwu1123/daily-ai-safety`，access 选 push）。
- 切到 `main` 并拉最新：`git checkout main && git pull origin main`。
- 日期一律用美东时间：`TZ=America/New_York date +%F`，下文记作 `TODAY`。

## 1. 找新内容

```bash
NODE_PATH=/opt/node22/lib/node_modules node tools/monitor.js
```

脚本会抓取 `tools/sources.json` 里的每个来源，把不在 `tools/seen_urls.txt` 里的链接写进 `tools/out/new_candidates.json`（`candidates` 是新链接，`errors` 是抓取异常）。

- 某个来源报 `no links found` 或其它错误时，重跑一次。还不行，就在日报末尾的"监控状态"里写明是哪个来源、什么错误。不要因为一个来源失败就整天不出日报。
- 候选里可能混有导航页、标签页、作者页、旧文章（例如页面改版后才露出来的旧链接）。逐条判断，不是文章的直接忽略。

## 2. 逐条判断

对每个真正的新文章，先抓全文：把候选写成 `[{id,url,title,date}]` 存成 JSON，然后运行 `NODE_PATH=/opt/node22/lib/node_modules node tools/fetch_texts.js <items.json> <texts_dir>`。页面很短、只有一个 arXiv/PDF 链接时，运行 `tools/addpaper.sh <texts_dir>` 把论文正文附上。openai.com 的页面偶尔会被 Cloudflare 拦，重试几次即可。

确认发布日期：以页面上写的日期为准。

- 发布日期在最近 3 天内，或者发布时间不明但确实是新出现的：算作"今日更新"。
- 明显更早发布、只是现在才被检测到：不写进日报的"今日更新"。如果它符合收录规则，照常建笔记补录，并在日报的"补录"一节里列一行。

然后按下面的规则分类。

### A. 建成笔记的 technical research

收录规则见 `README.md` 的"收录规则"，要点如下：

- **Anthropic（`--lab Anthropic`）**：只收 alignment.anthropic.com 和 anthropic.com/research/team/alignment 上的文章，这两个页面上的新文章全部收录。anthropic.com/news、anthropic.com/research 其它团队的内容只进日报，不建笔记。同一工作两边都有时合并为一条，另一版本用 `--also-*` 附上。
- **OpenAI（`--lab OpenAI`）**：alignment.openai.com 上 "Research and Releases" 列出的文章全部收录，包括它链接到 openai.com 的条目。Misalignment Reports / Notices 加 `--category "Misalignment Reports and Notices"`（会放进 `papers/OpenAI/Misalignment Reports/`）。openai.com/news 的其它内容只进日报。
- **METR / Apollo / UK AISI / FAR.AI / Goodfire / Transluce / Redwood**：只收实证/技术研究，包括论文、研究博客、技术笔记、模型评估报告、事故调查，以及对具体失败模式或安全技术的技术性分析。下面这些不建笔记（但可以进日报）：
  - 新闻、政策评论、组织动态、招聘、融资
  - AI 进展或时间线预测
  - 战略 essay
  - research agenda
  - 入门指南、书单、建议类文章
  - 论文 review 或讲解
  - 播客
  - 纯工具发布（没有研究结果的）
  - Goodfire：只看 research 页，不收生物、基因组、材料等科学应用类工作。
- **Alignment Forum（`--lab "Alignment Forum"`）**：只收 AF 帖子（不看普通 LessWrong）。作者里必须至少有一位是上述 9 家 lab 的研究员，lab 研究员作为合著者的 MATS / Anthropic Fellows 项目也算；Redwood 写作项目参与者、GDM、独立研究者等不算。先看它是不是已经发在 lab 主页上：已经在 lab 主页上的不建 AF 笔记，如果那篇 lab 文章还没收录，就作为对应 lab 的笔记收录。lab 主页上有、但不在我们给该 lab 划定的收录范围内的，也不收。同样只收实证/技术研究。来源行写成 `Alignment Forum（<lab>；<作者>）`。
- 同一工作在 lab 自己的多个页面（论文页 + 博客）都有时，合并成一篇笔记，用 `--also-url/--also-title/--also-label` 附上另一版本。
- 两家 lab 联合发布的同一份工作只建一篇笔记，`--lab` 写两次（例如 `--lab METR --lab "Redwood Research"`），另一家的链接用 `--also-*` 附上。

收录步骤：

1. 按 `tools/STYLE.md` 写简读（中文，一整段，风格和长度参照样例）。涉及攻击、jailbreak、网络攻击评估、sandbox 逃逸、事故里的具体手法，或生物/化学相关内容时，同时遵守 `tools/SENSITIVE_NOTE.md`：只写到摘要层面，不写任何可操作细节。
2. 从 `tools/TAGS.md` 的词表里选 1–4 个主题标签（只能用词表里的原词）。
3. 新建笔记（`--date` 必须精确到日，用原文标注的发布日期）。脚本会打印这篇笔记的双链，例如 `[[papers/METR/2026-10-23 标题|笔记]]`，写日报时要用：

```bash
python3 tools/new_note.py --lab <lab> --title "<原标题>" --url "<主链接>" --source "<来源名>" --date YYYY-MM-DD --tags 标签1,标签2 --summary-file <简读文件> [--also-url ... --also-title ... --also-label ...] [--category ...]
```

`--lab` 取值：`Anthropic`、`OpenAI`、`METR`、`Apollo Research`、`UK AISI`、`FAR.AI`、`Goodfire`、`Transluce`、`Redwood Research`、`Alignment Forum`。来源名沿用已有写法，例如：

- `Anthropic Alignment Science Blog`、`Anthropic Research`
- `OpenAI Alignment Blog`、`OpenAI Blog`、`OpenAI Misalignment Report`
- `METR Research`、`METR Notes`、`METR Blog`
- `Apollo Research`、`Apollo Blog`
- `AISI Research`、`AISI Blog`
- `FAR.AI Blog`、`FAR.AI Publications`
- `Goodfire Research`
- `Transluce`、`Transluce Docent Blog`
- `Redwood Research`、`Redwood Blog`

### B. 只进日报的其它更新

上面这些来源上所有其它新内容（新闻、政策、组织动态、招聘、活动、播客、预测和战略类文章等）都写进日报的"其它动态"。有两个来源要先筛：

- Anthropic 的 anthropic.com/news 和 anthropic.com/research（非 alignment 团队）
- OpenAI 的 openai.com/news RSS

这两个只挑和 safety / alignment / security / policy / 治理 / 风险 / 事故 / interpretability / 社会影响相关的条目，纯产品、商业、客户案例、招聘广告直接跳过（不写进日报，但要标记为已见）。

## 3. 写日报

文件路径：`daily_report/<年>-<月>/<TODAY>.md`。月份不补零，例如 `daily_report/2026-3/2026-03-05.md`、`daily_report/2026-10/2026-10-23.md`。文件夹不存在就新建。

格式：

```markdown
# AI Safety 日报 · YYYY-MM-DD

检查范围：README 中收录的全部 lab 与 Alignment Forum（含新闻等非研究类更新）。

## 研究更新（已建笔记）

- **[标题](链接)** · Lab · 来源名 — TL;DR：一到两句话说清楚做了什么、最重要的发现是什么（中文，约 40–90 字）。→ [[papers/<lab>/<笔记文件名>|笔记]]（直接用 new_note.py 打印的双链）

## 其它动态

- **[标题](链接)** · Lab · 类型（新闻 / 政策 / 组织动态 / 活动 / 预测 / 观点 等） — 一句话 TL;DR。

## 补录（较早发布、今天才检测到）

- **[标题](链接)** · Lab · 发布于 YYYY-MM-DD → [[papers/<lab>/<笔记文件名>|笔记]]

## 监控状态

- 各来源检查正常。 / - <来源>：<错误>
```

- 没有内容的小节直接删掉；"监控状态"始终保留。
- TL;DR 比笔记里的简读短得多，只保留最核心的一两点。
- 当天所有来源都没有任何新内容时，也要生成日报。正文写"今日无更新。"，再加"监控状态"一节。

## 4. 收尾

1. 把所有候选标记为已见（包括忽略掉的导航页和不相关条目，以免明天重复出现）：`node tools/monitor.js --mark-seen`。
2. 如果还有手动判断为"已处理"但不在候选里的 URL（例如 `--also` 链接），也追加进 `tools/seen_urls.txt`（保持排序、去重）。
3. 提交并推送到 main：

```bash
git add -A
git commit -m "Daily update YYYY-MM-DD"
git push origin main
```

推送前先 `git pull --rebase origin main`，因为用户的电脑和手机也会往仓库推送自己的笔记。万一出现冲突，一律保留用户那一方的改动（每日任务只新建文件，正常不会冲突）。网络错误按 2/4/8/16 秒间隔重试。

4. 最后用一两句话汇报：今天有几条研究更新、几条其它动态、收进了哪些文件、有没有监控异常。
