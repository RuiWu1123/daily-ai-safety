# 使用说明：电脑和 iPhone 同步阅读、书写

整体结构：

```
电脑 Obsidian ⇄ GitHub 仓库 ⇄ iPhone Obsidian
                    ↑
             每天的定时任务写入
```

三个地方都通过 GitHub 同步。两台设备上都需要装两个插件：**Git**（负责同步）和 **Dataview**（负责生成索引表格）。

## 一、准备：生成一个 GitHub 令牌（iPhone 要用，电脑也可以用）

1. 在浏览器打开 GitHub，点右上角头像 → **Settings** → 左侧最下面 **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**。
2. 填写：
   - Token name：随便起，比如 `obsidian`
   - Expiration：选最长的期限（到期后要重新生成一个，填回插件里）
   - Repository access：选 **Only select repositories**，再选 `daily-ai-safety`
   - Permissions → Repository permissions → **Contents** 选 **Read and write**
3. 点 **Generate token**，把生成的那串字符复制下来，存到备忘录或密码管理器里。它只显示这一次。

## 二、电脑（Mac 或 Windows）

1. 安装 Obsidian：<https://obsidian.md>（免费）。
2. 把仓库下载到电脑。最简单的是装 **GitHub Desktop**（<https://desktop.github.com>），登录后选 File → Clone repository → `RuiWu1123/daily-ai-safety`，选一个本地文件夹。
   - Windows 还需要装 git：<https://git-scm.com>。Mac 第一次用时如果提示安装开发者工具，点安装即可。
3. 打开 Obsidian → **打开本地文件夹作为仓库**，选刚才下载的 `daily-ai-safety` 文件夹。
4. 装插件：设置 → **第三方插件** → 关闭"安全模式" → **浏览**，分别搜索并安装、启用：
   - **Dataview**
   - **Git**（作者 Vinzent）
5. Git 插件设置（设置 → 第三方插件 → Git）：
   - **Auto commit-and-sync interval**：填 `10`（每 10 分钟自动提交并同步你的改动）
   - **Auto pull interval**：填 `10`
   - 打开 **Pull on startup**（每次打开 Obsidian 时先拉取最新内容）
6. 从 `README` 或 `index/最近更新` 开始看。

## 三、iPhone

1. App Store 安装 **Obsidian**。
2. 打开 Obsidian → **创建新仓库**，名字填 `daily-ai-safety`。**不要**勾选"存储在 iCloud"，选存在"我的 iPhone"上（iCloud 和 git 一起用容易出问题）。
3. 装插件：设置 → **第三方插件** → 关闭"安全模式" → **浏览**，安装并启用 **Git** 和 **Dataview**。
4. Git 插件设置里填：
   - **Username on your git server**：`RuiWu1123`
   - **Password/Personal access token**：粘贴第一步生成的令牌
   - **Author name / Author email**：你的名字和邮箱（用于提交记录）
5. 从屏幕顶部往下拉打开命令面板，输入 `clone`，选择 **Git: Clone an existing remote repo**：
   - 地址填：`https://github.com/RuiWu1123/daily-ai-safety.git`
   - 问目录时，选择克隆到仓库根目录（直接回车或选 vault root）
   - 问是否克隆 `.obsidian` 配置时选 No
   - 第一次克隆需要一两分钟。完成后完全退出 Obsidian 再重新打开。
6. 回到 Git 插件设置，同样打开 **Pull on startup**，把 **Auto commit-and-sync interval** 设为 `10`。
7. 手动同步：命令面板输入 `git`，选 **Git: Commit-and-sync**。

## 四、写笔记的建议

- **自己的笔记都写在 `my_notes/` 里**：论文笔记是只读的参考资料，不需要改。在笔记里输入 `[[` 可以按标题搜索并引用任何论文笔记；打开一篇论文笔记时，右侧"反向链接"面板会列出所有引用过它的笔记。
- 想引用论文里的某一节，可以写 `[[论文笔记名#简读]]`；想把简读直接嵌进自己的笔记，写 `![[论文笔记名#简读]]`。
- **避免冲突**：同一篇笔记不要在电脑和手机上"同时"修改。换设备时，先等 Obsidian 打开后自动拉取一下（或手动执行一次 Commit-and-sync）再动笔。
- **标签**：每篇论文带有主题标签，点标签可以看到同主题的所有论文；`index/按主题` 页面按主题汇总。

## 五、常见问题

- **索引页只显示代码，没有表格**：Dataview 插件没装或没启用。
- **iPhone 同步报错 401 / 403**：令牌过期或权限没选 Contents: Read and write。重新生成一个，填回 Git 插件设置。
- **提示冲突（conflict）**：打开出冲突的文件，删掉 `<<<<<<<`、`=======`、`>>>>>>>` 这几行标记，保留想要的内容，再执行一次 Commit-and-sync。
