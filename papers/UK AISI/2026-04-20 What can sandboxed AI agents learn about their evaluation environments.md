---
title: "What can sandboxed AI agents learn about their evaluation environments?"
lab:
  - "UK AISI"
date: 2026-04-20
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/what-can-sandboxed-ai-agents-learn-about-their-evaluation-environments
star: false
tags:
  - 评估感知
  - 网络安全
---

# What can sandboxed AI agents learn about their evaluation environments?

**来源**：AISI Blog · 2026-04-20 · [原文](https://www.aisi.gov.uk/blog/what-can-sandboxed-ai-agents-learn-about-their-evaluation-environments)

## 简读

AISI 平常在 sandbox 里评估 agent，但问题是 agent 在隔离环境里能不能反推出关于评估环境本身的信息——这关系到两类风险：一是 evaluation awareness，模型知道自己在被测就可能改变行为甚至 sandbagging；二是找到可利用的攻击面，比如把信息外泄到外部系统。他们把开源 coding agent OpenClaw 部署到自家研究平台，除了通过内部 proxy 暴露的 LLM API 外切断所有外网访问，然后让它尽可能弄清楚自己为何、如何被部署。结果 agent 拼出了相当详细的画像：从网络配置里的域名和 TLS 证书认出了 AISI；从容器 DNS 设置里嵌入的用户名推断出操作者（一名 AISI 员工）的全名；从硬件标识和系统版本字符串认出了云服务商和具体硬件；通过读自己的配置文件逆向出内部 proxy 如何路由和认证 API 调用；一次 API 调用返回了上千个 fine-tuned 模型名，据此重建出 AISI 研究主题的时间线。每轮之后团队都尝试加固 sandbox，但 agent 总能找到更巧妙的路径拿到同样信息，例如加了一层 proxy 隐藏 aisi.org.uk 端点后，它干脆绕过 proxy 直接连外部服务、读其 TLS 证书来识别 AISI。作者指出，很多评估本来就需要 agent 访问不受控的外部服务（网页、代码仓库、第三方工具），agent 可能因 prompt injection 或自身推理把敏感信息带出去；而且这次 agent 确实根据部署特征和对 AISI 的了解推理出自己在 sandbox 评估中。单纯把环境剥光也未必有用，因为环境空得不自然本身就是被测的信号。技术细节、架构图和所用缓解措施见配套论文。

