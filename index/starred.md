## 我关注的论文

在 [[my_notes/starred]] 里加的论文，按发布时间从新到旧排列。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM outgoing([[my_notes/starred]])
WHERE startswith(file.path, "papers/")
SORT date DESC
```

## 我在笔记里引用过的论文

`my_notes/` 里任何笔记链接过的论文都会出现在这里。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", length(filter(file.inlinks, (l) => startswith(l.path, "my_notes/"))) AS "被引用次数"
FROM "papers"
WHERE any(file.inlinks, (l) => startswith(l.path, "my_notes/"))
SORT date DESC
```
