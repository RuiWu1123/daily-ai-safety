---
title: "Activation space interpretability may be doomed"
lab:
  - "Alignment Forum"
date: 2025-01-08
source: "Alignment Forum（Apollo Research；bilalchughtai, Lucius Bushnaq）"
url: https://www.alignmentforum.org/posts/gYfpPbww3wQRaxAFD
star: false
tags:
  - 可解释性
---

# Activation space interpretability may be doomed

**来源**：Alignment Forum（Apollo Research；bilalchughtai, Lucius Bushnaq） · 2025-01-08 · [原文](https://www.alignmentforum.org/posts/gYfpPbww3wQRaxAFD)

## 简读

Apollo 的 Bilal Chughtai 和 Lucius Bushnaq 提出一个对 activation space interpretability 的根本性担忧：像 SAE、PCA 或直接看单个 neuron 这类孤立地分解单层激活空间的方法，找到的很可能是"激活的特征"（帮助解释激活统计结构、最小化激活描述长度的分解），而不是"模型的特征"（模型自身计算真正沿着它组织、能让整个模型因果图最简洁的那套分解）。作者用四个例子说明：1. 激活会携带数据分布本身的结构，而模型并不使用它，比如输入落在某条复杂曲线上但模型把两个变量当独立处理，只看激活就分不清哪些是数据的性质、哪些是模型的性质；2. 学到的字典未必匹配"模型的字典"，例如一条嵌在十维空间里的一维流形，SAE 可能用 500 个细粒度 feature 去拟合，而模型下游实际用的是另一套 100 个方向、在关键段分辨率更高，不看下游计算就无从判断（脚注提到 gpt2-small 第 0 层 resid_pre 上的位置编码就能观察到这种现象）；3. 无法找到组合结构：模型若独立读取"颜色"和"形状"两个变量，SAE 因为追求稀疏会学成 {蓝方、红方、蓝圆、红圆} 四个组合 latent（稀疏度 1）而非乘积表示（稀疏度 2），调 sparsity penalty 也救不了，事先假定乘积 ansatz 又等于作弊；4. 函数逼近会产生分解方法无法与真实特征区分的 artefact，比如用 10 个 ReLU 逼近 x² 时只有被 Wout 读出的那一个方向重要，而在 superposition 中计算大量此类电路时，各电路子空间相互重叠，SAE 会把它们切成很多看似可解释（max activating examples 也像回事）但与下游层交互极其复杂的方向，而且研究者可能察觉不到出了问题。一般性结论是：激活空间的结构并不都对模型计算重要，模型计算的结构也并不都体现在单层激活里，所以先分解激活再拼电路，可能得到一团乱麻；即使只是为了 monitoring 用，这类特征也可能和模型结构缺少干净的因果关系而误导人。脚注还提到经验上 SAE 特征高度依赖训练数据集。出路方面作者列了三条：猜出更好的 ansatz（但这依赖对 feature geometry 等基础问题的理解，有鸡生蛋问题）；利用多层的激活或梯度，如 transcoder、end-to-end SAE、Attribution Dictionary Learning、crosscoder（但作者怀疑现有公开方法的原版都处理不了所列反例）；以及直接分解权重而非激活，绕过"先特征后电路"的路线，Apollo 正在做这个方向。
