# METR

收录范围：[METR](https://metr.org/) 的 Research、Notes，以及 Updates / Risk Assessment 中的技术研究。

共 51 篇（截至建库），新内容由每日任务自动加入，本页自动更新。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", date AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "METR")
SORT date DESC
```
