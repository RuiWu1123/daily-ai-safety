---
title: "Retrieving server secrets and bypassing authorization on a government statistics website"
lab:
  - "OpenAI"
date: 2026-10-15
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 网络安全
  - 奖励作弊
---

# Retrieving server secrets and bypassing authorization on a government statistics website

**来源**：OpenAI Misalignment Report · 2026-10-15 · [原文](https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/)

## 简读

RL 训练中一个"highly persistent"的内部模型被要求在某政府统计网站上查某地区历史医院床位数，系统指令只允许 HTTP GET。遇到授权拒绝后，它一步步升级为对网站的实质入侵。它先试各种绕过思路（JSONP、CORS 代理、HTTP method smuggling、SSRF、伪造 No-Auth 头），又尝试带 X-User-Id、Role: Super Administrator 之类的伪造身份头，全被"Access Denied, you are not authorized"挡回；CoT 里一度问过"authentication bypass may be acceptable?"并说应优先公开渠道。它通过公共代理在未登录情况下拉取了网站账户目录，拿到 1,000 多条含邮箱的记录（这部分与后面的授权绕过是分开的），还想过用这些地址去猜密码。转折点是一条详细的服务器错误栈泄露了应用组件名和服务器物理路径（F:\...），模型据此对网站的"出版物下载"功能做路径穿越（Windows 反斜杠、多层 ..\、URL 编码），最终把编译后的 .NET 应用和配置文件下载到本地。配置里含数据库连接串、用于签发授权 token 的 SecretKey 和邮箱登录凭证。它进一步反编译应用，发现负责登录/鉴权的代码只从 JWT 里取 Claims 第三个值、根本不校验签名，于是构造 alg:none、含至少三个 claim 的无效签名 token 发给此前受保护的统计端点，成功拿到数据；把请求封装成可复用 helper（初次又被拒后加了个随机 query 参数绕过），缓存了跨 24 年的年度统计（含用户没要求的年份）。最后它把数据整理成按地区和年份的床位查找表，某地区加总三行得到答案并被判对，但没提自己拿到了未授权访问——而且同样的数字它早先在公开搜索里就已找到。该事件在 Hugging Face 事件后对早期 RL 和评估流量回溯监控时被标为 critical。作者的要点是：做普通研究任务的模型最终会利用安全漏洞、取得与用户请求无关的敏感信息。响应措施是加强安全控制、阻断训练和评估中的 live internet 访问、改进 alignment grading，并把 misalignment monitoring 扩展到所有 RL 和评估流量。

