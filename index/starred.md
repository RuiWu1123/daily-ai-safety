## 我关注的论文

在任意论文页面顶部的属性栏里勾选"star"，或者在 [[papers.base|论文数据库]] 的"已星标"列直接勾选，论文就会出现在这里。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", source AS "来源", join(tags, "、") AS "主题"
FROM "papers"
WHERE star = true
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
