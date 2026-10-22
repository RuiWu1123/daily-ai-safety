# 全部论文

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", date AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE true
SORT date DESC
```
