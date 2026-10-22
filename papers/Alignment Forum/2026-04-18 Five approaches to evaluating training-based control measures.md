---
title: "Five approaches to evaluating training-based control measures"
lab:
  - "Alignment Forum"
date: 2026-04-18
source: "Alignment Forum（Redwood Research；Alek Westover, sebastian_prasanna, Julian Stastny, Vivek Hebbar）"
url: https://www.alignmentforum.org/posts/mDcHzdoxB6sh3w2zG
star: false
tags:
  - 监控与控制
  - 评估方法
---

# Five approaches to evaluating training-based control measures

**来源**：Alignment Forum（Redwood Research；Alek Westover, sebastian_prasanna, Julian Stastny, Vivek Hebbar） · 2026-04-18 · [原文](https://www.alignmentforum.org/posts/mDcHzdoxB6sh3w2zG)

## 简读

Alek Westover 等人的方法论短文。training-based control 研究训练方法能多大程度约束 misaligned 模型，核心场景是让可能 scheming 的 AI 被"逼着"好好做安全研究。文章比较评估训练方法有效性的五条路线：1. YOLO，等模型足够强时直接在生产中 A/B 测试，无需外推，但研究质量难评估、信号慢、届时人手紧张、临场才测浪费时间，模型还可能察觉测试并操纵结果；2. malign init，由保守 red team 在合法动作内造的合成 misaligned 模型（如 Password-Locked Models、Sleeper Agents，禁止密码学后门等不自然机制），能放进与真实高度类似的场景、保守性让 blue team 的胜利更可信，但可能与自然 scheming 差别大、双方权限难定、深植行为可能需要接近后训练量级的训练；作者特别指出现有 malign init 都会被"训练模型像海盗一样说话"这类无原则方法轻易打败，所以目前不是好代理；3. 相对真实但做了手脚的训练过程产出的模型（如 Natural emergent misalignment、Alignment Faking），更贴近真实、对开发者更相关，但昂贵、迭代慢、可能需在实验室内做，blue team 可能赢得太轻松，难以发现只在更高能力才出现的问题（如 sandbagging），还可能加速能力；4. 类比，包括 mundane misalignment（sycophancy、reward hacking）和抽象类比（拒绝有害请求、让遵循 CCP 叙事的 AI 变诚实），省时且行为可能深植于模型，但不一定 bad-coded、无法研究研究破坏这类结构性场景，且有能力外溢；5. 认真想，迭代快、能跳过无用分支、不易过拟合当前模型，但有些经验事实想不出来，而我们对训练和泛化的理解很不原则化。结论：在需要用可能严重 misaligned 的模型自动化安全研究之前，应有一份排好优先级的技术清单，当务之急是先列清单并靠思考做初步排序，再视机会成本做实证评估。

