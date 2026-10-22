---
title: "Investigating the Indirect Object Identification circuit in Mamba"
lab:
  - "FAR.AI"
date: 2024-07-18
source: "FAR.AI Publications"
url: https://www.far.ai/research/investigating-the-indirect-object-identification-circuit-in-mamba
tags:
  - 可解释性
---

# Investigating the Indirect Object Identification circuit in Mamba

**来源**：FAR.AI Publications · 2024-07-18 · [原文](https://www.far.ai/research/investigating-the-indirect-object-identification-circuit-in-mamba)

## 简读

现有的 interpretability 技术能不能迁移到新架构？Mamba 是一个合适的测试对象：它是线性递归的 state space model，scaling 能和 Transformer 竞争，而且出现在大多数技术之后。Danielle Ensign 和 FAR 的 Adrià Garriga-Alonso 把 circuit 分析工具改造到 mamba-370m 上（这是 IOI 准确率约 96% 的最小 Mamba 模型），部分逆向了它的 IOI circuit。实验主要用 3 名字模板，因为 2 名字的任务太简单，结果会误导。1. layer 39 是关键瓶颈：resample 和 zero ablation 都指向 layer 0 和 layer 39；贪心地找允许跨 token 传信息的最小层集合时，layer 39 每次都在，而且总是第一个被加入（layer 15 也每次都出现），82% 的情况下不需要 layer 0，说明 layer 0 多是就地计算。另外，移除约一半的层几乎不影响准确率，这在 GPT-2 Small 上也复现了。2. layer 39 用 convolution 把名字信息往后挪一个位置：cosine similarity 图上的信号线总在名字之后一格，对 conv slice 做 ablation 也支持是 layer 39 自己做的平移，为什么这样做还不清楚。3. 名字在 layer 39 的 SSM 中是线性表示的：“减去当前名字的平均激活、加上目标名字的平均激活”在 95% 以上的情况下能把输出改成另一个名字；名字第一次和第二次出现时的表示互不兼容。4. layer 39 基本只往最后一个 token 写输出：去掉它所有非末位的输出连接，准确率只从 85.2% 降到 83.8%。最后他们改造 positional Edge Attribution Patching 自动找出一个 IOI circuit；ACDC 和 EAP 都得到稀疏的图，但 layer 39 之外还有不少活动，说明前面的层也有 cross-talk。作者认为这是 circuit 类工具在 Mamba 上也好用的初步证据，下一步想分析 39 层之前的 cross-talk，并用 SAE 做更细的 feature circuit。代码已开源。

