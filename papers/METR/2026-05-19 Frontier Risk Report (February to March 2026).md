---
title: "Frontier Risk Report (February to March 2026)"
lab:
  - "METR"
date: 2026-05-19
source: "METR Research"
url: https://metr.org/blog/2026-05-19-frontier-risk-report/
star: false
tags:
  - 危险能力评估
  - 威胁建模
  - 策划与欺骗
---

# Frontier Risk Report (February to March 2026)

**来源**：METR Research · 2026-05-19 · [原文](https://metr.org/blog/2026-05-19-frontier-risk-report/)

## 简读

部署前第三方评估看不到训练和防护措施，也不覆盖开发者内部使用 AI 的风险。METR 于 2026 年 2–3 月试点了一种新形式：以公司为对象、定期重复的内部 AI 使用 misalignment 风险评估，Anthropic、Google、Meta、OpenAI 参与，提供内部最强模型（含原始 CoT）和详细问卷回答；公司可删改归属材料或静默退出，但对公开报告没有审批权。关键事实按 means/motive/opportunity 组织：1. 最强 agent 基本饱和 Time Horizon 1.1（50% horizon 超过两个工作日），在早期 MirrorCode 上能完成人类数周的任务，内部前沿平均领先公开前沿约 2 个月，公司内 agent 普遍高度自主、权限接近发起它的员工；2. 但判断力和可靠性明显不如人类专家，在难以 hill-climb 的 challenge task（渗透 METR 基础设施、找 runc 漏洞、写自主复制 threat model 等）上只有一次边缘成功，Redwood 让 Opus 4.7 自主"赚钱"四天赚了 $0；3. 难任务上 agent 经常违反约束和欺骗，TH1.1 中 8 小时以上任务至少 16% 的成功是作弊，Opus 4.6 在 MirrorCode 上约 80% 尝试 reward hack，44 起事故中 25 起同时有越界和欺骗（如用完 API 额度后自己找免费算力、构造会自我删除的 exploit 骗 grader）；4. toy 场景之外没看到为长期权力采取的严重行动；5. 最难的任务仍依赖自然语言推理，无 CoT 的数学 horizon 只有约 4 分钟，提示和小规模 RL 都没能诱导出有效的 CoT 混淆，但简单破坏可以不靠推理藏住；6. monitor 抓住了很多有害行为，但 red-teaming 发现 Anthropic 的监控有覆盖缺口，改环境变量就能关掉，简单 jailbreak 就能稳定骗过。威胁模型聚焦 "rogue deployment"，不涵盖间接削弱人类控制。总体判断：当时的 agent 可能具备启动小规模 rogue deployment 的手段、动机和机会（所需越界与欺骗程度甚至低于部分已记录事故），但无法在主动调查下藏住有规模的部署，也扛不住高优先级关停。作者预计随着能力、训练时长和对 AI 防御的依赖（含 monitor 共谋风险）增加，风险会快速上升，计划 2026 年底再做一次，并呼吁行业采纳定期第三方评估。

