# 直接操作url
# 文件内容的左侧会显示该文件的行号。假如我们点击第 10 行的行号，这一行就会被高亮标记为黄色，
# 同时 URL 末尾会自动添加“#L10”。使用这个 URL，程序员们在交流时，就可以将讨论明确指向某一行。
# 另外，如果将“#L10”改成“#L10-15”，则会标记该文件的第10～15 行

# 比如我们想查看 4-0-stable 分支与 3-2-stable 分支之间的差别，可以像下面这样将分支名加到 URL 里
# https://github.com/rails/rails/compare/4-0-stable...3-2-stable

# 假如我们想查看 master 分支在最近 7 天内的差别，可以像下面这样这样将时间加入 URL
# https://github.com/rails/rails/compare/master@{7.day.ago}...master

# 假设我们想查看 master 分支 2013 年 1 月 1 日与现在的区别，可以将日期加入 URL。
# https://github.com/rails/rails/compare/master@{2013-01-01}...master


# Issue
# 在软件开发过程中，开发者们为了跟踪 BUG 及进行软件相关讨论，进而方便管理，创建了 Issue。
# 管理 Issue 的系统称为 BTS（Bug Tracking System，BUG 跟踪系统）。
# issue支持markdown语法，可以通过添加标签来分类

# 设置里程碑，就可以用 Issue 来管理任务
# 在 GitHub 上，如果给 Issue 添加源代码，它就会变成我们马上要讲到的 Pull Request。Issue 与 Pull Request 的编号相互通用

# Pull Request  
# 如果想获取 diff 格式的文件，只要像下面这样在 URL 末尾添加 .diff 即可。
# https://github.com/用户名/仓库名/pull/28.diff
# 同理， 想要 patch 格式的文件， 只需要在URL末尾添加 .patch 即可

# 