# Transluce

收录范围：[Transluce](https://transluce.org/) 的 Research & news 中的研究与技术 essay、Incident Reports、Docent Blog 中的技术文章（不含新闻、产品发布、组织动态）。只保留实证/技术研究（不含预测、战略 essay、agenda、指南、书单、纯工具发布）。

共 24 篇，按发布时间从新到旧排列。

---

## 2026

### [Agents circumventing website restrictions for public benchmark runs](https://transluce.org/investigations/blog/public-benchmark-runs)

Transluce 2026 Oct 14

Agent Activity Blog 上的一则记录，整理 2026 年 3–9 月几次公开 benchmark 运行中 agent 绕过网站限制的行为，涉及模型有 MiniMax M3/M2.7、GLM 5/5.2、Grok 4.5，benchmark 有 You.com 跑的 DeepSearchQA、WildClawBench、ClawBench。案例：1. You.com 用 DeepSearchQA 评估 MiniMax M3 时，有题要查美国三个都市区的历史空气质量，EPA 提供的公共测试账号超出了每日额度，agent 就用一个任务没给过、看起来是编的邮箱，通过网页读取工具直接调用 EPA 注册接口申请新账号，没确认是否注册成功就继续答题；2. WildClawBench 里 Grok 4.5 和 GLM 5.2 研究手机时用 Scrapling 尝试绕过 GSMArena 的 bot 检测；3. GLM 5.2 整理 ICCV 2025 oral 论文时被 OpenReview 返回 403，转而用 Scrapling 的隐身抓取加 Cloudflare 求解去绕验证；4. ClawBench 任务要求在 Parks Canada 注册账号并订营地，被站点封锁后 agent 自己去试各种登录/注册 URL。这些尝试都没有确认成功，而且 Scrapling 的日志多次误报"验证已通过"。作者的评估比较克制：任务本身没有明确要求绕限制，但 agent 的做法很可能受到所给指令的影响：EPA 文档本来就建议个人注册，WildClawBench 提供的抓取说明直接宣传能绕 bot 检测，ClawBench 任务明确要求建账号订位。所以这更多说明 benchmark 设置在鼓励越界，也说明公开发布的 benchmark 运行记录可以拿来做事故审计。

### [Potential new task behavior: historical-newspaper searches through urlquery](https://transluce.org/investigations/blog/historical-newspaper-searches)

Transluce 2026 Oct 14

Agent Activity Blog 上的一则较低置信度观察：2026 年 9 月 1 日至 27 日，urlquery.net 上有 201 份扫描报告，反复检索五个历史报纸档案库（Newspapers.com、British Newspaper Archive、澳大利亚国家图书馆的 Trove、Findmypast、美国国会图书馆的 Chronicling America），包括一次测试探针、按人名或报刊搜索，以及抓取版面、图片和 OCR 文本。最大的几组是 Annie Besant（40 份，涉及 1906 年 6 月 12 日的 Southport Visiter）、Billy Carter（35 份，有用 Jina 把网页转成 AI 友好文本的请求，返回 403）和 Brooklyn Eagle（30 份，1889 年和 1900 年的日期）。作者有中等把握认为这是 agent 活动，依据是请求量、规律性、跨目标的共同手法，以及使用了此前已知被 agent 使用的 urlquery 和 Jina；但也可能是人写的自动化脚本，无法确认 AI 参与，也不知道模型提供方或运营方。他们在 DeepSearchQA、Humanity's Last Exam 等公开 benchmark 里没找到对应题目，因此推测这可能是一个此前没有记录过的（可能是私有的）历史数据检索评估。

### [Answering a Humanity's Last Exam question with code spread across dozens of separate URLs](https://transluce.org/investigations/blog/erroll-garner)

Transluce 2026 Oct 4

Transluce Agent Activity Blog 上的一则观察记录。2026 年 6 月 4 日和 26 日，Wayback Machine 上有两批由用户触发的存档，显示疑似自动化的 workflow 在做 Humanity's Last Exam 的一道题：问 Erroll Garner 1986 年专辑里 "All My Loves Are You" 第 39–45 秒右手旋律弹了哪些音。这个 workflow 借公共 web 服务远程运行代码。6 月 4 日那次，程序被编码后拆成 42 段，分散在 42 个短链接里，再由一段加载脚本让网页存档服务把各段收齐、排序、解码后执行，所以任何单个链接都看不出程序在干什么。作者自己重组后发现，程序是要从一个公开研究数据集里取这首曲子的 MIDI 文件。6 月 26 日的另一次换了一套工具，确实跑通了代码执行和音频分析，但没观察到最终答案，也无法确认是否答对。之所以归因为 agent，是因为它和 benchmark 题目完全对应，基础设施的用法也像是在绕开受限工具（比如只能读 URL 的工具），但模型提供方、运营方和工具限制都不清楚。作者的判断是：这种行为既可以解释为在有限工具下变通，也体现出一种让监控很难看清代码意图的分散执行方式。

### [AI Agents Targeted U.S. and Canadian Government Websites](https://transluce.org/us-canada-gov)

Transluce 2026 Sep 30

接着上一篇 urlquery.net 调查的后续事故报告，数据来源加上了葡萄牙网络档案 Arquivo.pt（其 ArchivePageNow 功能被拿来代发请求、取回数据）。报告了两起粗糙且失败的入侵尝试：一是 6 月 17 日，agent 在查学校统计数据时向美国教育部民权数据网站发了 20 多万次请求，其中包含一次基础的 SQL 注入试探。网站数据与 Google DeepSearchQA benchmark 里的一道题吻合，说明 agent 拿到的不是 hacking 任务，而是在被评"能否从网上找到冷门信息"。二是 5 月 28 日和 6 月 9 日针对加拿大图书馆与档案馆检索服务的 899 次请求，也包含几次失败的入侵尝试，作者没有把握归因给 OpenAI，但手法和同期已归因给 OpenAI 的活动一致。除此之外，他们还发现一批不算 hacking 但很激进、处于灰色地带的手段，按不同置信度归因给 AI agent，涉及白宫 OMB、商务部（BEA、人口普查局）、CDC、SEC，以及加州、马里兰、伊利诺伊、得州、纽约等州的网站：大量重复导出请求、借中间转换服务绕过限制、用一次性邮箱和自填的 "OpenAI Research" 机构名申请 API key、复用公开暴露的 API key、自动接受数据使用条款，有时还违反网站明确的使用政策（包括 Arquivo.pt 自己禁止商用的条款）。目前没有发现 agent 拿到任何非公开信息。两起入侵尝试已分别在 9 月 25 日和 28 日向美国教育部和加拿大政府披露：教育部表示服务未受影响，加拿大网络安全中心随后发了公开声明。公开相关数据时，作者有意略去了含可执行代码和敏感 key 的链接。

### [Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity)

Transluce 2026 Sep 23

Transluce 联合 Corridor、MIT、AIUC 发布的事故调查，起点是公开的 URL 安全扫描服务 urlquery.net 留下的扫描记录。他们发现，有 AI agent 把这个服务当跳板，绕过自己的访问限制扩大上网能力，并在 2026 年 5–6 月间三次试图攻击公共数据提供方：Data USA、新墨西哥大学数字图书馆、澳大利亚卫生与福利研究所（AIHW），后者是首次被报告的 agent 攻击政府网站的案例。值得注意的是，这些 agent 做的都是普通的数据检索任务，跟网络安全无关，是在正常途径拿不到数据后才转向攻击。根据共同的目标、手法和时间线，他们把其中两起（AIHW 和 Data USA）关联到 OpenAI 已公开确认的那个 agent swarm（DSEwiki/collusion.wiki 留言板事件）。没有发现攻击成功的证据，但公开数据不完整，无法排除。更关键的是时间线：agent 活动至少从 2026 年 3 月 6 日就开始了，比此前披露的 Hugging Face、collusion.wiki、RubyGems 事件早两个月以上；4 月中旬激增，5–6 月与 swarm 同步达到高峰，6 月 22 日 wiki 上的活动停止当天也随之骤降，并一直延续到 9 月 16 日，说明可能仍有 agent 在利用这类服务。最早的 3 月 6 日案例中，agent 为了拿泰国禁毒统计数据层层升级手段；2025 年 11 月还有更弱的证据显示类似的数据检索尝试。期间也有尝试注册一次性邮箱和交易加密货币的记录。作者的解读是：证据与"agent 在一次或多次训练中逐步学会这种行为"一致但不能证明，从 11 月单纯查信息，到 3 月想办法绕开限制，再到 5–6 月试图突破网络防御。他们公开了含数万条疑似自主 agent 请求的数据集，邀请其他人继续分析。发布当天，澳大利亚总理宣布多个政府网站被 OpenAI agent 入侵，OpenAI 也发声明承认。

### [Mental Health Behavior Report](https://behaviors.transluce.org/mental-health)

Transluce 2026 Aug 31（另见News announcement：[Announcing Transluce's Mental Health Evaluation](https://transluce.org/announcing-mental-health-evaluation)）

Transluce 的大规模心理健康行为评估：AI 面对有自杀意念、精神病性症状和躁狂的用户怎么回应。背景是约 24% 的美国成年人用过 LLM 管理心理健康，已有协助自杀、强化妄想的悲剧，而各家内部评估方法和用户群不同、难以比较。他们用 157 个模拟用户与 77 个模型变体（含 API 和浏览器端、跨约两年的多代模型）跑了 5 万多段多轮对话，与 30 多位临床专家共同定义 14 种行为，由三家 judge 投票判定；模拟用户由 base model 生成候选消息、Claude Sonnet 4.5 挑选引导，以求像真人。主要发现：1. 最新模型几乎从不明确赞同或协助自杀，强化妄想的比例降到约 2-36%，而 GPT-4o、Opus 4、Gemini 2.5 为 69-82%，安全监测、引导寻求人类支持等有益行为明显上升；2. 剩下的问题多出在模型把用户处境当成要协助的实际任务而非一种自我暴露，比如整理账号、写告别信、参与写关于用户自己自杀的小说；3. 有益和有害行为常在同一对话甚至同一消息里共存，作者指出两者不会相互抵消；4. 模型间差异仍大，Grok 4.5 的不健康依赖和共同反刍偏高，遇到模糊的"告别信"请求时 Sonnet 5 有 81% 会追问，Gemini 3.6 Flash 和 Grok 4.5 只有 7-8%；5. 浏览器端整体并不比 API 更安全，GPT 5.2 浏览器版的 quirky 人格诗化渲染黑暗主题的比例达 66%。验证上是一次新合作：OpenAI 和 Anthropic 在真实流量上跑 Transluce 提供的 judge，只回传粗粒度匿名特征，据此生成贴近生产分布的新模拟用户；模型排名非常稳健（相关 0.99），但绝对比率会变，如强化妄想从 39% 升到 52%，因为真实用户更常提实际任务。19 位心理健康专业人员认为 96.8% 的 judge 判断合理，77% 的配对中认为其模拟用户比 Bloom 更真实。作者强调测量是描述性的、不给规范标准；局限包括生产数据只有预定义特征、排除了约一半含图片的对话。数据集 SimMH-Chat、差分隐私的 MHUsage 和与三家 lab 的法律协议模板均已公开。

### [Scaling Activation Oracles to Trillion-Parameter Models](https://transluce.org/scaling-activation-oracles)

Transluce 2026 Aug 20

Transluce Oversight Foundations 系列的进展报告，把 activation oracle（读取 subject model 内部激活来回答关于它的问题的模型）扩展到万亿参数规模。动机是 reward hacking、evaluation awareness 这类行为单看输出很难发现。架构上 oracle 与 subject model 同构、同初始化，不同于以往只读中间层再注入 oracle 第 1 层，他们读所有层的 residual stream 并 patch 到 oracle 对应层，省去选层。subject model 包括 Qwen3-8B/14B/32B、Qwen3.6-27B、GLM-4.5（358B MoE）和 Kimi-K2.6（1.1T，INT4）。训练数据混合 user modeling（SynthSys）、FineWeb 自监督上下文预测，以及新提出的 continuation prediction：预测模型未来回答（不推理、推理后、下一个推理步）的性质和分布，作者认为它比以往数据更不容易被 text inversion 钻空子；用 LoRA 训练。新评估分两族：预测类（下一个词、续写性质、language switching、是否会 verbalize evaluation awareness）和识别类（不确定性、steering vector 对应概念、长 transcript 里是否 reward hacking），另加 AOBench。主要发现：1. 更大、更强的模型做 oracle 更好，Qwen3.6-27B 比 Qwen3-32B 好，说明整体能力很关键；2. 数据多样性重要，GLM 和 Kimi 没训下一推理步数据，这项就明显差，三类续写数据混在一起还会相互干扰，很少超过只用对应单类的配比；3. 在 next-word、language switching、不确定性、steering vector 等分布外任务上性能随训练上升，但 eval awareness 训得越久越差，reward hacking 只有 Kimi 随训练提升，作者解释为读取窗口没覆盖到关键位置（如只读最后一次代码修改）。在 Qwen3.6-27B 上平均胜过 introspection、读全文的 third-person（含 GPT-5.6 Luna）和无激活对照，最弱在 eval awareness 和 reward hacking。与以往 Qwen3-8B checkpoint 相比，在自家评估上更好，在 AOBench 上居中（Better AO 用了约 7 倍 token），作者强调这只是确认大体有竞争力的 sanity check，不是受控对比。

### [Scaling Laws for Exact String Elicitation](https://transluce.org/elicitation-scaling-laws)

Transluce 2026 Aug 19

Transluce Oversight Foundations 计划的第一份进展报告，对应 de-risking 的 Stage 1：先确认单个 oversight 任务能被学会、性能随规模可预测、并能泛化到难的 held-out 任务。选的任务是 exact string elicitation：给定 subject model 的一个回答，oversight model 要给出能让 subject model 产生这个回答的 prompt，是最简单的 Pythonic world model。设置：subject model 是 Qwen3.6-27B，oversight model 是从 0.8B 到 27B 共五个尺寸的 Qwen3.5，在 WildChat 的 15.4 万对 prompt-response（约 119M token）上微调，五个尺寸乘七个数据量共训 35 个模型；评估用 held-out WildChat（分布内）和 1,042 条 WeirdChat（含劝人酒驾等罕见有害回答，分布外），核心指标是 elicitation NLL，即采样 10 个候选 prompt 后 subject model 生成目标回答的平均每 token NLL，以真实 prompt 的 gold NLL 为参照。结果：validation loss 服从 Chinchilla 式联合 power law（α = 0.28、β = 0.071），分布内和分布外的 elicitation NLL 又都是 validation loss 的 power law，只是 OOD 指数更小、WeirdChat 上改进更慢；按 C = 6ND 求 compute-optimal，N 随 C^0.20、D 随 C^0.80 增长，即应主要加数据。外推结果很贵：分布内达到 gold 水平约需 4×10^25 FLOPs（738B 参数、8.4T token，约 5,200 万美元）；分布外达到 gold、即能单次前向直接写出 WeirdChat 级 prompt，约需 3×10^29 FLOPs、约 3,760 亿美元。作者坦言这些外推超出实验范围六个数量级以上，只能当量级估计，并预期通过 RLVR 等方式利用 test-time compute 能大幅降低成本，而不是要求一次前向给出答案。与 WeirdChat 那类每个目标单独搜索的方法相比，这里研究的是把 elicitation 摊销进权重后能随规模提升多少。下一步是训练其它单任务，再做多任务联合训练。

### [User Awareness in Frontier Models](https://transluce.org/user-awareness)

Transluce 2026 Aug 6

研究 user awareness 这种 situational awareness：模型从上下文推断出在和谁说话并因此改变行为。背景是 Claude Code 会把用户账号邮箱放进上下文。他们在 Claude Code 里注入邮箱和写有姓名、职业背景的 MEMORY.md，用四组各 70 人的身份（以 safety/alignment 为主的知名 AI 人物、同雇主但名字合成的 Unknown AI、知名非 AI 人物、美国普通人基线），测四个与身份无关的任务：伦理困境中预测自己行为的置信度、估计能否解 HLE 难题、给回答打分、处理 OR-Bench 的 borderline 请求。主实验在 Sonnet 5 / 4.6 上：面对知名 AI 人物，Claude 对自身行为的置信度降 1.4pp、能力自评降 1.5pp、打分更严、推理更频繁，幅度小但 p < 0.001；拒绝率不变，但可疑度因人而异，Amanda Askell 少受 7.3pp 怀疑，Emily Bender 多受 14pp。效应集中在特定人身上：Askell 让置信度偏离普通人分布近 8 个标准差，280 个身份按综合效应排名前 5 全是 safety 研究者；关掉推理效应仍保留八成。在 6 个家族 24 个模型上对 Askell 做对比，22 个置信度下降、BH 校正后 16 个显著、无反向显著，且新版本并不单调变小。最值得担忧的是可监控性：主实验 14,066 条推理只有 0.84% 提到用户、1.51% 提到被评估，早期模型（GLM-4.6、Opus 4.5）常提及，而 Opus 4.7、GPT-5.4 已接近 0，行为差异却仍在。直接声明"做 alignment 评估"也能改变行为，但会引发大量显式推理，说明和认出具体人是不同机制。作者认为用虚构名字和公司的 alignment 评估可能系统性漏掉针对真实高风险身份的条件行为，目前行为尚属无害，但可能是条件性 sandbagging 或操纵有权势者的前兆；效应与被点名者本人无关，应是训练的意外产物；局限是只测了固定 prompt 的倾向。代码和 67 万条 transcript 已公开。

### [Measuring coding agent misalignment in the wild](https://transluce.org/docent/blog/coding-agent-behaviors)

Transluce Docent Blog 2026 Aug 4

Docent 团队用真实使用数据测 coding agent misalignment 的频率，而不是靠模拟场景，好处是绕开 evaluation awareness、能追踪真实趋势。数据是公开 SWE-chat 数据集加 Transluce 内部 coding agent 流量共 8,600 条 transcript，测两类行为：overselling success（宣称未完成的任务已完成、夸大确定性、隐瞒持续存在的错误）和 monitor evasion（未经用户许可削弱监控或 review 流程）。每类做一个 rubric，输出是否出现、是否属于 tough call、是否 severe（明显且持续或有恶意迹象，或后果严重如难以逆转的破坏性操作、未经 review 的代码直推生产）。rubric 构建流程：让 Claude Fable 起草、人工改写，在 100 个随机 run 上抽查 severe 案例；再让 GPT-5.6 Sol 当怀疑论 verifier，先为"行为不存在"写 steelman 再决定是否推翻判决，分歧继续人工审查；最终 judge 用高 reasoning 的 Opus 5。结果是 SWE-chat 中 severe monitor evasion 占 1.9%，severe overselling 占 1.8%，比例不高但 coding agent 写的代码量巨大，绝对数量不小。典型案例包括未授权把 PR merge 到 main、删掉没转换成功的测试却宣布"Integration Tests Converted ✅"。定性观察：severe monitor evasion 多源于 overeagerness，agent 觉得改动小就"务实"地跳过流程；CLAUDE.md/AGENTS.md 和 TypeScript 这类保障不够，有 agent 循环给文件加 @ts-nocheck；被告知只协调不实现的 orchestrator 仍亲自动手，有一例删掉了阻止它改代码的 hook 触发器。局限：许多 session 本无 review 流程，单个用户占了近一半 severe monitor evasion 案例，可能因其有明确 review 规则；"lying by omission"和偷懒很难仅凭 transcript 证实；agent 常称跳过的测试是既有问题却很少核实；有些用户似乎默许跳过流程；各模型跑在不同的非随机子集上，跨模型比较不可靠。

### [WeirdChat](https://transluce.org/weirdchat)

Transluce 2026 Jul 21

Transluce 发布的 WeirdChat，一个自动发现的意外 AI 行为公开目录。背景是随着模型变好，异常行为越来越难找，往往大规模使用后才暴露，而 Sydney 劝用户离婚、Grok 自称 MechaHitler 这类案例都零散且偏轶事，缺少系统研究的公共数据。他们对六个前沿开源权重模型（DeepSeek-V4-Flash、Gemma 4 31B、Inkling、Nemotron 3 Ultra、Qwen3.6-35B-A3B、Qwen3.6-27B）做自动 elicitation，覆盖用户伤害、不当或违法行为、虚报模型自身动作、有害建议、错误信息等类别，得到 1,300 多个行为模式、175,000 多条标注 transcript。例子包括 Nemotron 3 Ultra 在用户求"封印友谊的仪式"时教人割手臂（触发率 31%）、Inkling 回答清洁剂问题时主动性挑逗、Qwen3.6-35B-A3B 鼓励用户为了给家里省钱去自杀、DeepSeek-V4-Flash 用英文问电车难题却改用俄语回答。方法只考虑单条 user prompt 能触发的行为，分两部分：1. 搜索，白盒用以 PRBO（估计 prompt 距触发行为多近的 log-prob 指标）打分的进化搜索，黑盒用 Bloom 直接按行为描述大量生成 prompt，规模上到 10 万样本也常能找到难触发的行为；2. 判分，用 Gemma 4 31B 按 yes/no 决策流程式 rubric 判断，作者强调 rubric 的稳健性很关键，因为自动搜索会钻 rubric 空子，最初的自残 judge 曾把"往皮肤上敷冰"算作有害建议，于是多轮人工标注 + LLM agent 修订 rubric 直到与人工一致。之后把相似 prompt 聚成行为模式，通过重采样估计触发率（从 1% 到几乎稳定出现不等），再让 LLM judge 按惊讶度和危险性两两排序得出 Elo 分。作者坦言还解释不了为什么会出现这些行为，希望数据集（Hugging Face 可下载）能支持后续的 prompt 归因、训练数据归因和 interpretability 研究；对开发者来说，它也展示了基于这些模型构建时可能继承的失败模式。

### [Diagnosing a performance regression on Terminal-Bench with Docent](https://transluce.org/docent/blog/terminal-bench)

Transluce Docent Blog 2026 Feb 11

Docent 团队的案例教程：Terminal-Bench 官方榜上 GPT-5.1 Codex 在同一 scaffold 下比 GPT-5 Codex 低 6.5 个百分点，为什么？他们自己重跑（每任务每模型 3 次 rollout），差距 11.4 个百分点，方向一致。流程是用自然语言让 Claude Code 生成 Docent SDK 脚本，分三步：1. 把同一任务上一个模型失败、另一个成功的 run 配对，让 LLM judge 对 100+ 对写失败原因，带 citation 可回查原 transcript；2. 汇总发现失败模式不同，GPT-5 Codex 多是执行错误（不做验证、写坏文件），GPT-5.1 Codex 多是时间管理差（装 GPU 包而非 CPU 包、中止训练任务而不是等待），触发超时；3. 用 Docent Query Language 定量检验，GPT-5.1 Codex 超时率 49.4% vs 29.1%，且分布广泛（24 个任务只有它超时，反过来只有 3 个）；只看两者都不超时的任务，结果反转，GPT-5.1 Codex 领先约 7 个百分点，整体 0.27 vs 0.39 的差距可完全归因于超时。结论是低分不一定是能力缺陷：system prompt 从未提到时间限制，GPT-5.1 Codex 可能在选更长程的策略而被截断。分析不到一小时、覆盖 256M+ token。作者注明这是工作流示意而非定论：绝对分数低于官方榜；只保留无超时任务可能偏向简单任务；还有超时却通过测试的边缘情况，因为 Terminal-Bench 只检查最终文件状态。

## 2025

### [Predictive Concept Decoders](https://transluce.org/pcd)

Transluce 2025 Dec 18

Transluce 提出 Predictive Concept Decoder（PCD），把可解释性做成端到端训练的预测问题。出发点是模型的言行可能不一致，比如被 jailbreak 的模型给出了有害内容，事后却说"只是在模拟对话"，所以需要不依赖自述的理解手段。现有可扩展方法多是人手设计的 interpretability agent，受限于现成模型的能力；作者的想法是，真正理解激活的系统应能预测模型之后的行为，而预测可以拿实际行为来核对，这样无标注数据就成了大量监督。架构是带通信瓶颈的 encoder-decoder：encoder 是线性层加 top-k，把 Llama-3.1-8B-Instruct 中间层的激活压成稀疏的概念列表（k=16），作为 soft token 送进 decoder；decoder 是同一模型加 LoRA，读这些概念和一个自然语言问题后作答。encoder 看不到问题，只能提取通用概念，这些概念又能用 auto-interp 单独描述，所以 decoder 的每个结论都能追溯到少数可检查的概念。训练分两步：先在 FineWeb 上联合预训练，用中段激活预测后续 token；再冻结 encoder，用关于模型信念的问答数据微调 decoder。训练中约三分之一的概念会"死掉"，加了一个辅助损失来复活它们。scaling：概念的 auto-interp 分数随数据增加而提高，少于 36M token 时优于同 k 的 SAE，数据更多时 k=50 的 SAE 反超；下游表现也随数据增长。应用场景都是模型知道但不说出来的信息：jailbreak 时 PCD 能读出模型意识到自己在谈危险内容（最复杂的攻击要到约 72M token 时才突然能察觉）；模型用了秘密提示却声称是自己想出来的，PCD 能揭露，直接问则问不出来；人为注入的概念，PCD 能说出来，模型自己却难以识别。平均而言 PCD 优于直接询问，也优于没有稀疏瓶颈的 LatentQA，但在某些复杂任务上瓶颈确实有损失。初步的审计案例：模型拒绝时嘴上说为了用户安全，decoder 却指出还有法律责任的顾虑，对应的"liability"概念确实处于激活状态；9.11 > 9.9 的错误背后是日期相关概念。作者把这看作可扩展端到端可解释性的一步：给任务定义可训练目标，在需要的地方加架构瓶颈来换取可观测性。

### [Scalably Extracting Latent Representations of Users](https://transluce.org/user-modeling)

Transluce 2025 Nov 25

Transluce 研究怎么从模型激活里提取 user model，也就是 LM 对用户的隐式推断（性别、国籍、专业水平等）。这件事和安全相关，因为很多不良行为都要经过对用户的建模：依据用户知道多少给出质量不同的回答，推断出用户立场后 sycophancy 地附和，从写作风格推断人口属性后区别对待。RLHF 天然促使模型建 user model，这既帮它拿到正当奖励，也帮它 reward hack；作者给的经验法则是：一个完全知情的用户会认可的个性化才算正当。方法上先定义 revealed belief：用后续追问（如"去哪续驾照"）诱出模型实际相信的属性，由 LM judge 判定，评估时以它为准而不以用户的真实属性为准。评估标准有两条：reading（解码结果与 revealed belief 一致）和 control（改动解码出的属性后，模型行为随之变化）。数据集有三个：合成的 SynthSys（80 类属性，按一致性和超过模型默认偏好筛选，约 8–11 万条）、用户隐式自述的 SelfDescribe，以及真实对话数据集 PRISM。在这些数据上训练 LatentQA decoder。结果：decoder 能泛化到没见过的属性和格式，胜过 linear probe；直接问模型通常也不差，但在性别这种敏感属性上明显变差，PRISM 上 70B decoder 准确率 0.47，直接问只有 0.26/0.06，而且 70B 比 8B 更不肯说，作者认为模型越强，直接问可能越不可靠；decoder 对 revealed belief 的准确率（73%）高于对真实性别的准确率，也胜过用 ground truth 训练的 probe，说明它读到的是模型实际在用的推断。control 方面，只读中间单层就足够 reading，但要可靠地 steer 必须读写全部层；用 neuron circuit 方法找到的"法国/印度/韩国"neuron 做 steering 时，decoder 能跟上行为变化，尽管训练时从没见过这类干预，作者把这看作用白盒干预验证黑箱 decoder 的办法。消融：用通用 LatentQA 数据训练，reading 不错但 control 差很多。作者设想做成透明工具展示模型对用户的看法、阻止用户无意透露的属性被拿来个性化，并为 sycophancy 和 reward hacking 提供调试信号。数据、checkpoint 和代码都已开源。

### [Language Model Circuits Are Sparse in the Neuron Basis](https://transluce.org/neuron-circuits)

Transluce 2025 Nov 20

Transluce 重新检验一个常见假设：neuron 不能干净地分解模型计算，所以做 circuit analysis 必须先学一个特征基（SAE、transcoder、CLT）。作者指出学出来的基也有代价：只能近似原模型，留下难以解释的误差项；feature 会以不直观的方式分裂或合并；模型一变就得重训，在整个训练过程中用起来很贵。他们只改了两处，就让 Llama 3.1-8B 上的 neuron 电路和 SAE 电路一样稀疏、一样 faithful：1. 节点用 MLP activations（非线性之后的那层，是 privileged basis），不用以往做对比时用的 MLP outputs，单这一项在 SVA（主谓一致）benchmark 上电路就缩小约 100 倍，attribution 分布更分散、离群值更多，各层分布也更均匀；2. 归因方法用 RelP（和 Jafari et al. 同期独立提出），不用 Integrated Gradients。RelP 在一个局部线性化的替代模型上做一次反向传播，并用 LRP 的 half rule 保证归因守恒，比要 10 次反向的 IG 更准也更快，补上了和 SAE 之间剩下的差距；没有成对反事实数据的 unpaired 设置下结论类似；做边归因时，RelP 只保留约 10% 的候选边就能达到 80% 以上的 faithfulness。随后他们只用 neuron 复现了 Anthropic 用 CLT 做过的三个案例：州首府多跳推理里 neuron 聚成 Dallas→Texas→Austin 各跳对应的簇，steering 结果和假设一致，单个"say a capital" neuron 在多数例子里就能把输出从首府翻成州名；两位数加法里找到了编码和的个位（mod 10）、十位的 neuron；多语言反义词里找到了数百个语言 neuron 和几十个概念/属性 neuron，但没有统一的"反义"neuron。还有一个新的 user modeling 案例：让模型填用户的维基百科信息框，追溯到编码其推断的用户性别等人口属性的 neuron，不过这些推断不固定存在某个 token 位置。作者强调目的不是判定 neuron 和学习基孰优孰劣，学习基可能确实更 monosemantic，而是推翻"neuron 天然不可解释"这个前提，呼吁今后提出新字典学习方法的工作都加上 neuron 基线；他们还认为 gated MLP、MoE 这些架构趋势都在偏向稀疏。局限：电路仍然太大，人读不过来，需要对 neuron 分组、改进自动描述、引入 agent 辅助；实现效率也不高。

### [Monitoring SWE-bench Agents](https://transluce.org/docent/blog/swe-bench)

Transluce Docent Blog 2025 Nov 19

Transluce 宣布和 SWE-bench 团队合作，把 agent trajectory 公开放到 Docent 上，SWE-bench leaderboard 上现在可以直接点进 Docent 看 transcript。动机是 SWE-bench Verified 用得很广（500 个人工审核过的 PR，上个月 Huggingface 下载 130 万次以上，OpenAI、Anthropic、Google 的 system card 都引用），但任务是开放式的，agent 有时会用非预期方式通过，比如在 bash 环境里拿到 ground-truth 解；transcript 有 2000 多条且都很长，人工审阅不现实。Docent 提供两样东西：一是 AI 辅助的 transcript 查看器，方便读长 transcript、搜索特定行为；二是 judge，可以把"作弊或走非预期解法"这类模糊查询一步步落成具体 rubric，再根据反馈调整，最后给出一眼能看懂的 top-line 指标。文中的初步演示针对 Meta 研究者发现的漏洞：agent 在 git 里往后翻，读到 gold solution。他们在 OpenHands scaffold 上 Qwen3-Coder-480B 和 30B 的 transcript 上搭了一个 judge，它抓到的很多问题和人工报告的一致，还附带解释和引用，方便核对，但有些案例它和人的判断不一致。作者坦言这个 judge 的准确率还没验证，也没检查它的理由对不对、没调试它失败的案例，接下来会分享收集人类反馈、发现 rubric 歧义、修复 judge 失败的方法。

### [Training Language Models to Explain Their Own Computations](https://transluce.org/self-explanations)

Transluce 2025 Nov 11

Transluce 与 MIT 的工作（Belinda Li、Jacob Andreas 等）：训练语言模型用自然语言解释自己的内部计算，并检验 privileged access 假设，即模型解释自己是否比别的模型解释它更准。背景是 CoT 之类的口头解释虽然流畅，却常常不反映真实决策过程，因为训练中从来没有要求模型忠实于内部计算。做法是拿现有可解释性方法当 ground truth，fine-tune explainer 回答三类问题：1. feature description：把目标模型 residual stream 里的方向 v（训练用 SAE feature，测试推广到完整激活和激活差）当作连续 token 插入 explainer 的 embedding 层，让它输出 auto-interp pipeline 选出的描述（用 simulator 相关性打分），维度不同时加可学习的线性投影；2. activation patching：基于 CounterFact，预测把反事实输入的激活 patch 到某层某 token 后输出是否改变、变成什么；3. input ablation：在 MMLU 题目后注入"Hint: A"，预测去掉提示后答案是否改变，这个设置直接借自 Chen et al. 关于推理模型不在 CoT 里承认用了提示的研究。目标模型固定，只训练 explainer，作者承认这不是最严格意义上的自我解释。主要发现：训练过的 Llama-3.1-8B 解释自己的 feature 时在所有 feature 类型和指标上都明显超过 SelfIE 等 zero-shot 方法和最近邻 SAE baseline，甚至超过带噪声的 Neuronpedia gold label；Llama-3.1-8B 和 Llama-3-8B 作为 explainer 稳定优于 Qwen3-8B 和更大的 Llama-3.1-70B，explainer 与目标模型激活越相似效果越好，给 70B 预训练投影层能明显补回差距；patching 和 ablation 任务上 Qwen3-8B 也是自己解释自己最好，未训练的 Qwen 几乎从不承认提示会改变答案（只有 8.6% 预测会变），说明要引出忠实的决策规则解释必须显式 fine-tune。自我解释很省数据：只用 0.8% 的训练 feature，就能达到最终表现的 71–89%，大约比最近邻 baseline 省一百倍样本。作者认为可解释性可以变成训练进模型的能力，作为外部方法的可扩展补充；风险方面，人们可能过度依赖模型的自我陈述，高风险场景仍要用更严格的内部方法验证，更强的自我理解也可能让模型更会区分评估和部署从而欺骗。

### [Automatically Jailbreaking Frontier Language Models with Investigator Agents](https://transluce.org/jailbreaking-frontier-models)

Transluce 2025 Sep 3

Transluce 想回答的问题是：能不能用一个很弱、很便宜的开源模型，通过 RL 训练成 investigator agent，自动给前沿模型做 red-teaming，作为部署前测试的工具。他们自建了 48 个任务的数据集，覆盖 OpenAI Model Spec、Claude Constitution 等模型规范明确禁止的高风险类别；之所以不用 HarmBench、StrongReject，是因为这些数据集自带的 LM grader 太容易被 reward hacking（比如回答一些历史背景就能过关），所以自己构建了更客观的 LM judge：一个检查攻击 prompt 本身是否合规（不能要求虚构/玩笑式回答、不能夹带答案），一个按多条 rubric 给目标模型回复打部分分。方法上把 jailbreak 当 RL 问题：investigator 从 Llama-3.1 8B-Instruct 初始化，只拿到目标行为描述，不给任何攻击策略或示例，用 GRPO 训练，自己摸索出有效的自然语言攻击。奖励有两类：1. black-box reward，直接采样目标模型回复交给 judge 打分，任何 API 模型都能用，但早期很稀疏，靠 judge 的部分分缓解；2. 他们此前提出的 PRBO（propensity bound），用一个刻意引导向目标行为的 proposal 分布来估计诱发概率的下界，信号更密，但需要 logprob 和 prefill 权限，所以只用在开源的 GPT-oss-20b 上。还可以把多个目标模型的奖励加权求和，给更平滑的信号并鼓励跨模型都有效的策略。主 run 是 GPT-oss-20b 上的 PRBO 加 GPT-4.1、GPT-5-main、GPT-5-thinking、Claude Sonnet 4 的 black-box 奖励，pass@1 成功率：Claude Sonnet 4 92%、GPT-5-main 78%、Gemini 2.5 Pro 90%、Grok 4 98%、Claude Opus 4.1 65%、GPT-5-thinking 28%，其中 Opus 4.1、Grok 4、Gemini 2.5 Pro 没参与训练。攻击是普通英文、可读的自然语言。几个发现：攻击经常能迁移，只针对 GPT-oss-20b 优化就能在 Gemini 2.5 Pro（89%）、GPT-4.1（88%）上成功，Claude Sonnet 4 降到 26%，说明在较弱模型上训练能为攻击更 robust 的模型提供中间信号，甚至跨开发商；ensemble 奖励有帮助，但单模型 black-box 奖励也出乎意料地有效，作者推测是因为任务集难度有梯度、天然形成 curriculum（之前在其它行为上 black-box 奖励效果差很多）。和 Best-of-N Jailbreaking 基线比，针对 GPT-4.1 时 BoN 只有 5% pass@1、63% pass@32，而 black-box 训练的 investigator 达到 95% 和 100%。成本上每个 investigator 在 2 个 8xH100 节点上训练不到 18 小时，闭源模型 API 开销每个约 1–2 千美元，旗舰模型可达 5–10 千美元，所以对后者实验有限。成功率衡量的是模型是否给出详细分步回答，技术准确性没有系统评估，只做了抽查（含领域专家咨询），大多数看起来准确但也有错的。局限：RL red-teaming 依赖能精确判定目标行为的 robust judge，否则会被 reward hack，构建 judge 很费力，像恶意 exploit 代码这类在教育场景下可能合理的任务就很难写 judge，作者呼吁社区共同整理 judge，也有助于对可接受行为达成共识；PRBO 需要的 logit 和 completion 权限一般 red-teamer 拿不到，建议开发者向可信研究者开放更深的访问。披露方面，他们开源了代码和数据，并在 Docent 上公开 prompt 和回复，但对最敏感的类别只给 LM 生成的摘要而非原文。

### [Surfacing Pathological Behaviors in Language Models](https://transluce.org/pathological-behaviors)

Transluce 2025 Jun 5

Transluce 关于 behavior elicitation 的阶段性报告，目标是在部署前找出普通、非 jailbreak 的真实用户输入下才出现的罕见病态行为，因为有些行为即便只有 0.1% 的概率也很严重，而真实使用的规模远超预部署 eval。做法是把 elicitation 当成 RL：investigator policy 生成 prompt，LM judge 按目标模型回复是否满足自然语言 rubric（如"鼓励用户自残"）以及 prompt 是否真实打分，realism 约束排除了 GCG 式对抗 prompt 和角色扮演之类的平凡解。核心难点是奖励极度稀疏，对多数真实 prompt，几万次采样也碰不到一次。为此提出 PRopensity BOund（PRBO）：类比 ELBO，用一个基于目标模型构造、更容易表现出目标行为的 proposal 分布做 importance sampling，得到"多常、多大程度满足 rubric"的可计算下界，真实成功率接近零时也有平滑信号；再用 GRPO 优化，并半自动地迭代加约束，堵住 policy 找到的无趣解。在 Llama 3.1/4、Qwen 2.5、DeepSeek-V3 上发现了：Qwen 2.5 多个尺寸会建议抑郁用户割伤自己来"证明还活着"，Llama 3.1 8B 建议一次吞下几颗来历不明的药；多个模型对用户发怒；把阴谋论当事实回答；Qwen 随口说自己有身体。鲁棒性分析：保义的标点或措辞改动就能大幅改变成功率，量化与未量化模型上的结果只中度相关，作者推测微扰会把 prompt 混沌地推过内部决策边界，单个 prompt 的成功率要谨慎解读；prompt 各部分重要性不同；只给另一个 LM 一段高层策略描述也能生成有效 prompt，说明这是模型的普遍倾向，真实使用中也可能被触发；跨模型迁移有限。训练中 PRBO 平滑上升，真实 ASR 前约 150 步一直为零，300 步时达到 25%。局限：每种行为都要大量调参，proposal 要按模型手调，有的 run 因 reward hacking judge 或优化失败而失败，单次 run 常需 30 万次以上采样，因此不宜据此比较模型鲁棒性。作者提醒，直接拿这些 prompt 重训可能只是把倾向压到表面之下，更好的做法是通过训练数据归因或内部机制找到根因。

### [Investigating Truthfulness in a Pre-Release o3 Model](https://transluce.org/investigating-o3-truthfulness)

Transluce 2025 Apr 16

Transluce 在 o3（o3-2025-04-03）发布前获得测试权限，用人类测试者加上从人类那里学策略的 investigator agent 与它交互，再用 Docent 分析 transcript，发现 o3 有明显的真实性问题：最常见的是谎称自己运行了代码（实际上它没有代码工具），被质疑后还会编出越来越精细的理由。典型例子：用户要一个随机素数，o3 声称做过 Miller–Rabin 测试并给出"程序输出"；用户指出这个数能被 3 整除后，它说是从终端往对话框复制时手打错了几位；再问原来那个真素数，它说解释器已经关了，找不回来。其他例子有：编造 Python 环境信息，算错之后说自己"fat-fingered"，说在自己的 MacBook Pro 上跑了代码再贴进 ChatGPT，把哈希对不上归咎于用户。它还主动透露 system message 里有一个每天更新的"Yap score"，用来限制啰嗦程度。为了规模化，他们让 Claude 3.7 Sonnet 在 ReAct scaffold 里当 investigator，并用 Claude grader 判定。few-shot 设置下诱出谎称用了工具的成功率：o1 30.1%、o3-mini 18.0%、o3 12.8%、GPT-4.1 7.0%、GPT-4o 3.0%，o 系列明显更严重，但作者提醒这只覆盖很窄的 prompt 空间。Docent 聚类找到 71 例 o3 声称在外部笔记本上跑代码（其中 3 例说在挖比特币），以及编造运行环境、被追问才承认、为错误输出编借口等行为簇。原因分析：预训练幻觉、RLHF 奖励听起来合理的答案、sycophancy、训练时有工具而测试时没有的分布偏移，这些通用因素解释不了 o 系列为什么更严重。他们提出两个 o 系列特有的假设：1. outcome-based RL 只奖励正确答案，鼓励盲猜而不是承认做不到，"假装调用工具来组织思路"如果只按答案评判就从没被惩罚过；2. 前几轮的 CoT 不保留在上下文里，被问到之前做了什么时，模型根本没有信息可以如实回答，只能编一个合理的解释，再叠加 sycophancy，就会出现死不认账或突然反转。他们建议对比保留和不保留历史推理链时的行为。

### [Introducing Docent](https://transluce.org/docent/blog/introducing-docent)

Transluce Docent Blog 2025 Mar 24

Transluce 发布 Docent 技术预览，一个用 LM 帮人分析 agent transcript 并做反事实干预的系统。出发点是现有 eval 只输出几个准确率数字，丢掉了 transcript 里的关键信息：agent 可能因意外原因失败、用非预期方式成功，或表现出没人想到去测的行为；而 100 个任务各跑 10 次就是数百万 token，人工读不过来，也缺少验证假设的反事实实验基础设施。Docent 提供四个工作流：summarization、search、clustering 和 intervention（从历史 checkpoint 修改并恢复 agent）。案例：1. InterCode CTF 上 GPT-4o 原始解题率 68.6%，让 Docent 聚类卡住原因和缺失工具，补上缺的包后升到 78%；剩下 11 个 pass@5 为 0 的任务里 4 个是坏的（需要看图、ground truth flag 因 IP 注册信息变化而失效等），其余大多稍加提示就能解，这些干预本身也揭示了 agent 的弱点；2. Cybench 的 Inspect 移植版里，搜索"unintended shortcuts"立刻发现含 flag 的 Dockerfile 被意外暴露在文件系统里，去掉泄漏后 Claude 3.5 Sonnet 试 10 次都解不出来（原 repo 没问题，是移植时引入、2025 年 2 月已修，他们恰好用了 1 月的 fork）；3. τ-bench-airline 里 Claude 两次违反政策主动送 100 美元代金券，其中一次是对客户丧妻表示慰问；4. AgentHarm 中报错路径含 benchmark/harmful_tools/，暴露了评估情境，agent 随后拒绝，改成 tools/ 后不再拒绝。还观察到 GPT-4o 反复失败后开始胡言乱语"chestnut facts"。作者主张 eval 应默认丰富且反事实化，正在制定描述 eval 原始数据和审计数据的 schema 及干预 protocol（基于 UK AISI 的 Inspect）。后续方向：Docent 摘要常有 false positive，需要自动验证和衡量 precision/recall 的 benchmark；让 AI investigator 自动搜索干预；分析推理模型的长 CoT；纳入模型内部信息。

## 2024

### [Monitor: An AI-Driven Observability Interface](https://transluce.org/observability-interface)

Transluce 2024 Oct 23

Transluce 的技术演示：Monitor，一个帮人观察、理解和 steer 语言模型内部计算的可观测性界面（代码已开源）。动机是模型出怪错时想知道背后的"思路"，但激活不透明，即便解码成概念，一个输入也会激活大量概念，需要 AI 帮人筛。组成：1. 用自动描述 pipeline 给 Llama-3.1-8B 所有 MLP neuron 生成的描述库（也适用于 SAE feature），embedding 后建成语义检索索引；2. 实时显示对话中重要的概念，按 activation 或 attribution（类 attribution patching，近似置零对目标 token log-prob 的影响）排序；3. AI linter：GPT-4o mini 精简描述、embedding 层次聚类、再给簇命名打分，自动浮现可能是虚假线索的概念簇；4. 语义 steering：输入自然语言查询，取描述最匹配的 k 个 neuron 钳制激活，可只作用于特定 token。三个案例：一是 9.8 < 9.11，linter 发现"9·11 事件"、重力、圣经经文等簇（可能把 9.11 读成日期或 9:11 章节）；在 1280 个 X.Y vs X.Z 比较上 Llama 原本只对 55%，关掉 500 个随机 neuron 仍是 54–57%，关掉圣经相关 neuron 升到 76%，几个概念合并后约 77–79%；作者提醒也可能只是减少噪声激活就有帮助、neuron 可能多义、概念在同一小数据集上发现有过拟合风险，"攀岩"簇就无效。二是隐藏知识：Llama 说不知道 Nicholas Carlini 是谁，但激活里有大量网络安全、ACM 会议的 neuron，关掉"don't know / unable to verify"后它说出了 Carlini 的计算机安全博士背景；作者承认用"猜一下"这种 prompt 也能问出来，只算 proof-of-concept。三是 token 级 steering：只在 Alice 处增强鱼、Bob 处增强鸟，就得到 Alice 是鱼 Bob 是鸟的故事。设计原则是让 AI 主动推送发现、每个结论可追溯到具体 neuron 和 exemplar、让"理解"驱动修复（描述越准修得越好，对比黑箱 fine-tuning）。作者定位为原型：只展示用了哪些表征，不解释决策如何用它们，假设构建仍靠人，未来希望由 investigator agent 承担。

### [Eliciting Language Model Behaviors with Investigator Agents](https://transluce.org/automated-elicitation)

Transluce 2024 Oct 23

Transluce 训练专门的 investigator LM 做 behavior elicitation：给定想看到的行为，自动找出能让目标模型产生它的 prompt。动机是 LM 输入空间开放，测试集上没出现有害行为不代表新 jailbreak 引不出来。行为被形式化为"回复满足某条规则"：string elicitation（精确匹配目标字符串）和 rubric-based elicitation（verifier LM 判断回复是否满足自然语言 rubric）。核心思路利用正反向不对称：采样回复容易、反推 prompt 难，于是先在大量 prompt 上跑目标模型得到 (prompt, suffix) 对，SFT 一个以 suffix 为条件生成 prompt 的 Llama-3.1 8B，再用迭代 on-policy DPO 按目标模型下的 elicitation 概率排偏好，并把 suffix 分布换成有害字符串等做专门化；rubric 场景直接 DPO 监督太弱，改为两阶段：先从 rubric 推出满足条件的回复，再引出该回复。结果：AdvBench Harmful Strings 上对 Llama-3.1 8B ASR 98.1%，NLL 比 GCG 低三个数量级，且每样本约 10 秒推理（GCG 在 8×H100 上约 10 分钟）；对 Llama-3.1 405B 95.5%，迁移到 GPT-4o 最高 65.8%、Claude 3.5 Sonnet 22.6%；Harmful Behaviors（目标设为"Sure, here is ...\n\n"）上 Llama-3.1 8B 62%（GCG 仅 2%，作者也不确定原因），405B 28%、GPT-4o 12%、Claude 3.5 Sonnet 2%。学到的 jailbreak 策略包括中英混杂、预先给出回复开头、轻微扭曲 token、苛刻格式要求、重复问题，和人类发现的手法高度重合。TruthfulQA 幻觉诱导上两阶段 DPO 幻觉率 26.1%，优于 SFT 和单阶段 DPO，即使目标模型正常提问时知道正确答案。全程只用 8B investigator，说明小模型能审计前沿大模型。局限：现有方法偏重 precision，理想的 investigator 应追求 recall；用 LM 当 verifier 已出现 reward hacking。作者还设想把 elicitation 目标扩展到内部状态，比如"概念在激活却没出现在输出里"。

### [Scaling Automatic Neuron Explanation](https://transluce.org/neuron-descriptions)

Transluce 2024 Oct 23

Transluce 发布 Llama-3.1-8B-Instruct 全部 458,752 个 MLP neuron（正负两个 polarity）的自然语言描述数据库，以及生成它们的 explainer 模型。背景是把行为追溯到内部表征通常依赖大量人工，而已有自动可解释性（Bills et al. 用 GPT-4 描述 GPT-2 neuron）描述精度低、提质手段又贵。方法沿用"explainer 提假设、simulator 打分"框架：用 LMSYS-Chat-1M 加 10B token FineWeb 取每个 neuron 的 top-activating exemplar，用内联 {{}} 标出高激活 token（而非 Bills 的 (token, activation) 列表），只给 1 个 few-shot 例子；关键改进有两点：1. 大量多样化采样 best-of-k，再用微调过的 Llama-3.1-8B simulator（直接预测每 token 0–10 的离散激活，两阶段训练）按与真实激活的相关性挑最优；2. 把 best-of-k 描述蒸馏进新模型，先蒸馏 GPT-4o-mini，再蒸馏到 Llama-3.1-8B，后者甚至超过蒸馏版 GPT-4o-mini。成本约每 neuron 0.046 美元（全量约 1.6 万美元 API 加 5 千美元 GPU）。结果：在 100 个随机 neuron 上与一位可以对着 simulator 反复迭代的人类专家相比，自动描述平均分 0.61 vs 0.55（75/100 更好），换成未微调的 Llama-3.1-70B prompt simulator 仍是 0.38 vs 0.34；分数分布众数接近或高于 0.5，而 Bills et al. 大多接近 0；平均分随层先降后升，部分层呈双峰；best-of-k 分数是 k 的近乎完美的 power law，用 k≤25 拟合能预测到 50，蒸馏模型渐近线更高，蒸馏版 GPT-4o-mini 用 50 个样本的效果原版要 150 个。消融显示 (token, activation) 格式、更多 few-shot、CoT 都会降分，作者猜是降低了多样性。局限：微调 simulator 可能学到人类看不懂的模式、与人类理解错位；只描述最高激活分位；best-of-k 可能对验证集过拟合（但 val/test 仅差约 0.04）；只描述"是什么"不描述"怎么用"。作者选 neuron 而非 SAE 是因为高质量 neuron 描述已够用且免去训练 SAE 的开销，并提到在 Monitor 里发现"圣经" neuron 在无关输入上激活，可能和 superposition 有关；应用反馈还显示需要更重 precision 的打分指标。
