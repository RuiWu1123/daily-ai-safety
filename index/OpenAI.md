收录范围：[OpenAI Alignment Research Blog](https://alignment.openai.com/) 全部文章（含链接到 openai.com 的条目），另单列 [Misalignment Reports and Notices](https://alignment.openai.com/misalignment-reports/)。

共 48 篇（截至 2026-10-22），新内容由每日任务自动加入，本页自动更新。

## 研究与发布

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "OpenAI") AND !category
SORT date DESC
```

## Misalignment Reports and Notices

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE contains(lab, "OpenAI") AND category
SORT date DESC
```
