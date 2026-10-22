# 最近更新（近 30 天）

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", date AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE date >= date(today) - dur(30 days)
SORT date DESC
```

## 最近的日报

```dataview
LIST FROM "daily_report" WHERE file.name != "README" SORT file.name DESC LIMIT 14
```
