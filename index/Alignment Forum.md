收录范围：2025 年至今 [Alignment Forum](https://www.alignmentforum.org/) 上由上述 lab 研究员发布（含 lab 研究员合著的 MATS / Fellows 项目）、且未被其 lab 主页收录的技术研究帖。

共 59 篇（截至建库），新内容由每日任务自动加入，本页自动更新。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "Alignment Forum")
SORT date DESC
```
