# daily-ai-safety

个人 AI safety 研究收录，按 Obsidian 笔记库组织：一篇论文一个笔记，每篇有标题与原文链接、来源与发布日期、主题标签、中文简读。论文笔记是只读的参考资料，你自己的笔记写在 `my_notes/` 里，用 `[[...]]` 引用论文笔记。每天由定时任务自动加入新研究并写日报。

**电脑和 iPhone 上怎么用，见 [使用说明](SETUP.md)。**

## 从哪里开始看

- [我关注的论文](index/starred.md)：你在 `my_notes/starred` 里加的论文，以及你笔记里引用过的论文
- [最近更新](index/recent.md)：近 30 天的新论文和最近的日报
- [按主题浏览](index/by_topic.md)：按"奖励作弊""监控与控制""可解释性"等主题分组
- [全部论文](index/all_papers.md)
- 各 lab：[Anthropic](index/Anthropic.md) · [OpenAI](index/OpenAI.md) · [METR](index/METR.md) · [Apollo Research](index/Apollo%20Research.md) · [UK AISI](index/UK%20AISI.md) · [FAR.AI](index/FAR.AI.md) · [Goodfire](index/Goodfire.md) · [Transluce](index/Transluce.md) · [Redwood Research](index/Redwood%20Research.md) · [Alignment Forum](index/Alignment%20Forum.md)
- [每日日报](daily_report/)

索引页用 Obsidian 的 Dataview 插件自动生成表格，在 GitHub 网页上只会显示查询代码，请在 Obsidian 里看。

## 目录结构

| 位置 | 内容 | 谁来写 |
|---|---|---|
| `papers/<lab>/` | 每篇论文一个笔记，文件名是"发布日期 + 标题" | 定时任务新建，只读参考 |
| `daily_report/<年>-<月>/` | 每日综合日报（含新闻等非研究类动态，每条一两句 TL;DR） | 定时任务 |
| `index/` | 各 lab、全部论文、按主题、最近更新的自动索引 | 自动生成，不需要改 |
| `my_notes/` | 你自己的笔记，引用论文笔记 | 只有你 |
| `tools/` | 定时任务用的脚本和说明 | 不用管 |

定时任务只会**新建**论文笔记和日报，绝不碰 `my_notes/`，所以不会和你写的内容冲突。

## 收录规则

- 一项研究只记一篇笔记：发布在某 lab 自己主页上的，归到该 lab；只出现在 Alignment Forum、没有被 lab 主页收录的，归到 Alignment Forum。同一工作在同一 lab 的多个页面都有时合并为一篇，另一版本作为"另见"链接附上；两家 lab 联合发布的，笔记里同时标两家。
- 只收录实证/技术研究（论文、研究博客、技术笔记、模型评估报告、事故调查、对具体失败模式或安全技术的技术性分析）。不收新闻、政策评论、组织动态、招聘与融资公告，也不收 AI 进展/时间线预测、战略 essay、research agenda、入门指南与书单、播客、纯工具发布（这些会出现在日报的"其它动态"里）。Anthropic 与 OpenAI 按各自指定的页面全量收录，不做这层过滤。
- 收录范围：
  - Anthropic：[Alignment Science Blog](https://alignment.anthropic.com/) + [anthropic.com/research 的 Alignment team 页](https://www.anthropic.com/research/team/alignment)，全部历史
  - OpenAI：[Alignment Research Blog](https://alignment.openai.com/)，含 Misalignment Reports and Notices，全部历史
  - METR、Apollo Research、UK AISI、FAR.AI、Goodfire（只看 research 页，不含生物/基因组/材料等科学应用）、Transluce、Redwood Research：全部历史
  - Alignment Forum：2025 年至今，上述 lab 研究员发布（含 lab 研究员合著的 MATS / Fellows 项目）的帖子
- 简读格式：背景/动机 → 做了什么 → 主要发现 → 作者的解读、局限与结论。少数涉及攻击手法或生物/化学内容的条目只写到摘要层面。
