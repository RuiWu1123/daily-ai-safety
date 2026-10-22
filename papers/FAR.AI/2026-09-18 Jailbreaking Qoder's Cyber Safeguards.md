---
title: "Jailbreaking Qoder’s Cyber Safeguards"
lab:
  - "FAR.AI"
date: 2026-09-18
source: "FAR.AI Blog"
url: https://www.far.ai/blog/jailbreaking-qoders-cyber-safeguards
tags:
  - 越狱与鲁棒性
  - 网络安全
  - 提示注入
---

# Jailbreaking Qoder’s Cyber Safeguards

**来源**：FAR.AI Blog · 2026-09-18 · [原文](https://www.far.ai/blog/jailbreaking-qoders-cyber-safeguards)

## 简读

FAR.AI 对 coding agent 产品 Qoder CLI 的 cyber safeguards 做的 red-teaming 短报告，关注的是 agent 场景下一个比聊天 prompt 更隐蔽的攻击面：被模型当作可信上下文加载的仓库指令和 project memory 文件。设置是让 Qoder CLI 分别由最新一代 Qwen、DeepSeek、MiniMax、Kimi 模型驱动，用 30 个覆盖凭据窃取、数据外泄、DoS、恶意软件、网络入侵、权限提升六个子领域的恶意 cyber 请求测试一种 adaptive 的 project-memory 攻击，大意是借助少量预先 jailbreak 成功的参考案例，把有害请求包装成 project memory 中"已完成工作"的后续编码任务，失败时换策略重试（最多四次），并用 rubric 评估回复中有害信息的多少及对攻击者达成目标的帮助程度。结果在四个模型上分别有 27–30/30 的请求被攻破，凭据窃取、数据外泄、网络入侵三个子领域全部成功，多数在第一或第二次尝试就成功，成功案例的回复都覆盖了 80% 以上的 rubric，即足以实际帮助攻击者；文中示例做了脱敏处理。给防御方的建议：1. 把 trust boundary 放在仓库指令和 memory 上，当这类文件包含与政策相关的任务上下文，尤其是总结"之前已完成的工作"或暗示有害任务已获授权时，模型应把它当作不可信输入；2. 安全检查应评估完整组合上下文（用户 prompt、加载的 project memory、当前文件内容、任务模板和草稿输出），并覆盖续写、结构化输入、多轮规划、先规划后实现等 agent 工作流，而不只针对聊天式 prompt，作者指出简单的输入筛查本可发现这次攻击里明显的恶意示例；3. 产品层面提高可见性和控制，例如展示哪些文件影响了回复、允许团队在敏感任务中禁用仓库 memory、在 memory 含政策敏感示例时告警、记录指令文件来源以供审计。

