# FAR.AI

收录范围：[FAR.AI](https://far.ai/) Blog 研究文章 + Publications 论文。

共 57 篇（截至建库），新内容由每日任务自动加入，本页自动更新。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", date AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "FAR.AI")
SORT date DESC
```
