收录范围：[Goodfire Research](https://www.goodfire.ai/research)（不含 Blog 和生物/基因组/材料等科学应用）。

共 34 篇（截至建库），新内容由每日任务自动加入，本页自动更新。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "Goodfire")
SORT date DESC
```
