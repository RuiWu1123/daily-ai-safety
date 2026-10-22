---
title: "An overview of control measures"
lab:
  - "Redwood Research"
date: 2025-04-06
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/an-overview-of-control-measures
star: false
tags:
  - 监控与控制
  - 安全基础设施
---

# An overview of control measures

**来源**：Redwood Blog · 2025-04-06 · [原文](https://blog.redwoodresearch.org/p/an-overview-of-control-measures)

## 简读

Ryan Greenblatt 接着"Prioritizing threats for AI control"一文，盘点降低 misalignment 存在性风险的 control 措施。他先声明现在更重要的是 control evaluation 方法论，理想做法是走流程：先对抗性地分析 AI 可能造成的问题，再用 control eval 和 testbed 迭代决定具体措施，而不是先拍板"要上 XYZ"；但列清单仍然有用，因为能加速日后的迭代，某些类别（如反 steganography）适合单独研究，而且开发者到时可能很仓促。措施分三类，大致对应软件工程、ML 和安全三个现有领域：1. 非 ML 的软件基础设施，最重要的是：鲁棒、普遍、可挂接同步/异步监控的输入输出日志（需要安全团队支持，因为日志本身就是敏感信息集中地）；细粒度权限管理和 sandbox；支持在输出生效前监控、阻断、重采样的 scaffold（因此不能依赖 streaming）；artifact 和 job 追踪，把产物、任务、权限和产生它们的轨迹连成完整的因果图；记录 AI 自己看不到的上下文以供审查。次要的包括：可分组、可分级触发、最后一招可以直接断电的 shutdown 机制（借鉴算法交易，定期演练甚至随机停机，让停机不那么昂贵）；在线训练基础设施（可用 LoRA 按 silo 部署）；不让 AI 知道当前时间、是否被暂停过等多余信息（比如 KV cache 重算带来的数值差异可能泄露"刚被暂停重跑"）；管理（可能 opaque 的）记忆库，保持多个独立记忆库以去相关；廉价模拟环境用于红队和定罪调查；用定期发布签名加密日志的方式向第三方证明事故属实。2. AI 与人类组件，核心措施是：对每个动作运行的廉价监控（trusted monitoring、带 collusion busting 的 untrusted monitoring、coup probes），检测器更新后回扫历史动作；重采样与 defer 策略；逐级加码、最后才交给人类的自动审计层级；可借助 debate 等 recursive oversight、并持续被红队测试的人类审计流程；以及依托高度逼真合成输入的对抗评估和训练。较次要的有：事故上报、升级与停机流程（让多数 AI 不知道这个流程的状态，并测试它们看到伪造的"被抓"证据时会不会抢先发难）、trustedness evaluation、专门微调的红队模型、对坏动作发生率骤增的自动响应、由 AI 辅助的权限分配、追踪安全论证所依赖假设的 design basis。更投机的方向有：让 AI 相信虚假事实或给它错误的情境认知、精确的能力控制（unlearning、gradient routing，让不需要的 AI 不懂网络攻击和我们的控制措施）、配合在线训练的正则化、提升 trusted 模型的能力上限（哪怕更慢更贵）、去除分布偏移的 redaction、更精细的定罪手段、快速让人类跟上 AI 进展的培训材料、廉价的模型多样化、检测 treacherous turn 时的大幅分布偏移。专项对策包括 exploration hacking、steganography（尤其是 AI 从自己写的长文本中反推出当时的隐含状态）、一致性检查和任务分解、跨上下文检测 pro-AI bias 这类单看每个动作都无害的系统性偏向（要按重要性加权，防止它在不同群体上正负抵消）、数据投毒和说服等领域特定措施。3. 安全：基础设施本身要安全（AI 不能删日志），与防范人类内部威胁的措施大量重叠；比较不显然的是用硬件安全特性只允许 GPU 运行经签名的代码，由一个接口很窄的签名服务器记录 AI 跑的所有代码，以及在数据中心内部设上传和带宽限制，确保某些 GPU 上的任务不可能在偷偷训练强模型。他指出若公司已达到 SL5 级别安全，control 额外需要的安全改进不多，但更可能是在远低于 SL5 的条件下做 control。文章不涉及可解释性、latent adversarial training 和与 AI 做交易等方法；在"十个内部人"这种低投入情形下，应只挑其中一小部分来做。

