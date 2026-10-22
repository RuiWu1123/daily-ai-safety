---
title: "How are AI agents used? Evidence from 177,000 MCP tools"
lab:
  - "UK AISI"
date: 2026-03-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/how-are-ai-agents-used-evidence-from-177-000-mcp-tools
other_versions:
  - "https://www.aisi.gov.uk/blog/how-are-ai-agents-used-evidence-from-177000-ai-agent-tools"
tags:
  - 人机交互与社会影响
---

# How are AI agents used? Evidence from 177,000 MCP tools

**来源**：AISI Research · 2026-03-26 · [原文](https://www.aisi.gov.uk/research/how-are-ai-agents-used-evidence-from-177-000-mcp-tools)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/how-are-ai-agents-used-evidence-from-177000-ai-agent-tools)

## 简读

背景是 agent 正从生成内容转向直接作用于外部环境，但开发者、研究者和政府都缺少关于 agent 实际被拿来做什么、做多高风险的事的大规模证据，已有研究多是看 LLM 使用或少量平台数据。AISI 的 Merlin Stein（与 Bank of England 合作）换了一个观测层：监测公开的 MCP server 仓库（GitHub、Smithery），收集 2024 年 11 月到 2026 年 2 月间的 177,436 个 agent 工具，这是目前最大的 agent 工具数据集；再用 NPM 和 PyPI 下载量（覆盖 3,854 个 server、42,498 个工具）近似使用量。作者把工具的 action space 拆成五个维度：direct impact（perception / reasoning / action）、generality（窄 API 还是浏览器、任意代码这类不受约束的环境）、按 O*NET 职业映射的任务领域和 stakes、使用地域、是否由 AI 共同编写；分类由经人类专家验证过的 LLM judge 完成。主要发现：1. 规模暴涨，公开工具一年内从约 4,888 个增长到 177,000 个（36 倍），下载从 8 万增至 1,400 万；2. 从观察转向行动，action 工具占下载量的比例从 27% 升到 65%（注册公司发布的工具从 21% 到 71%），主要由 computer use 和浏览器自动化驱动；general-purpose 工具占下载比例从 41% 升到 50%，其中约 94–95% 带 action 能力，也就是说有实际后果的动作越来越多发生在最不受控的环境里，而不是受限的 API；3. 软件开发和 IT 占工具数的 67%、下载的 90%，多数 action 工具支持中等 stakes 职业，但金融是例外，高 stakes 金融职业的 action 工具比整体趋势预测的多，带支付执行能力的 MCP server 从 2025 年 1 月的 47 个增至 2026 年 2 月的 1,578 个，且集中在可能不可逆的加密货币交易；4. 下载约一半以上来自美国，其次西欧约 20%、中国约 5%（PyPI 偏西方，可能有偏差）；5. AI 正在给自己造工具，约 28% 的 server 检测到 AI 协助，新建 server 中这一比例从 6% 升到 62%，其中 Claude Code 占约三分之二。讨论部分认为 action space 扩张同时放大 misuse、misalignment/错误和结构性风险（比如同一底座模型的一次坏更新在大量高 stakes agent 上引发相关失败、"agent bank run"），而 general-purpose 工具让按工具粒度的治理更难，可能需要按调用上下文设权限、对大额转账等关键动作要求人类认证、agent ID 等。局限：MCP 只是工具分发渠道之一，结果是 action space 的下界；看得到工具发布和下载，看不到实际调用和使用场景；如果 agent 越来越多是按需自造工具，或者转向 general-purpose 工具，这种监测会越来越不起作用，作者建议后续去跟踪 skills、AGENTS.md 等更贴近具体任务的编排层，并为金融等领域建立系统性风险监测框架。

