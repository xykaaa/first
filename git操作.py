# git init——初始化仓库
# 执行了 git init命令的目录下就会生成 .git 目录。这个 .git 目录里存储着管理当前目录内容所需的仓库数据

# git status 查看当前库的状态，每一次操作都会改变状态

# git add filename 向暂存区添加文件,要想让文件成为 Git 仓库的管理对象，
# 就需要用 git add命令将其加入暂存区（Stage 或者 Index）中。暂存区是提交之前的一个临时区域

# git commit 命令可以将当前暂存区中的文件实际保存到仓库的历史记录中。通过这些记录，我们就可以在工作树中复原文件
# 记述一行提交信息,-m 参数后的 "First commit"称作提交信息，是对这个提交的概述
# 记述详细提交信息,如果想要记述得更加详细，加 -a，-a会直接提交所有修改的已跟踪文件，但不会提交不再暂存区的新创建的文件
# -a == add filename + -m
# git commit -am ""快捷提交
# 第一行：用一行文字简述提交的更改内容
# 第二行：空行
# 第三行以后：记述更改的原因和详细内容
# 如果在编辑器启动后想中止提交，请将提交信息留空并直接关闭编辑器，随后提交就会被中止

# git log——查看提交日志
# commit 栏旁边显示的“9f129b……”是指向这个提交的哈希值。Git 的其他命令中，在指向提交时会用到这个哈希值
# 如果只想让程序显示第一行简述信息，可以在 git log命令后加上 --pretty=short
# 只要在 git log命令后加上目录名，便会只显示该目录下的日志。如果加的是文件名，就会只显示与该文件相关的日志
# 如果想查看提交所带来的改动，可以加上 -p参数，文件的前后差别就会显示在提交信息之后。
# git diff命令可以查看工作树、暂存区、最新提交之间的差别
# 如果使用了git add 提交到暂存区，则什么都不会显示
# git diff HEAD命令，查看本次提交与上次提交之间有什么差别，等确认完毕后再进行提交
# 这里的 HEAD 是指向当前分支中最新一次提交的指针

# git branch——显示分支一览表,添加 -a参数可以同时显示本地仓库和远程仓库的分支信息。
# 左侧标有“*”（星号），表示这是我们当前所在的分支
# git checkout  - b——创建、切换分支
# (2) 回溯到某个 commit（进入“分离 HEAD”状态，不属于任何分支（detached HEAD））
# 不能正常提交，想提交需要创建新分支，或者回到主分支再合并刚才的操作

# 切换分支 git checkout 分支名
# 用“-”（连字符）代替分支名，就可以切换至上一个分支

# 不同分支是并行操作的,相互不影响

# git merge 分支名 ——合并分支
# 为了在历史记录中明确记录下本次分支合并，我们需要创建合并提交。因此，在合并时加上 --no-ff参数

# git log  -- graph——可以用图表形式输出提交日志
# git log --graph --online --all 输出所有分支的图表形式
# git reflog 查看所有head的变动分支切换合并提交等
# 功能	                    git reflog	                                             git log
# 作用	                 记录 HEAD 的变动历史	                                  记录所有提交历史
# 显示范围	             本地操作（包括 reset、checkout、merge、commit 等）	       所有提交（但无法显示 reset、checkout 记录）
# 能否找回丢失的提交	  可以（即使 commit 被 reset --hard 删除）	                不可以（reset --hard 后看不到被删除的 commit）

# git reset——回溯历史版本
# git reset --hard 哈希值,使用git reflog来查看每个节点的哈希值

# git commit  -- amend——修改上一条提交信息

# git rebase  -i HEAD~n(最新的n个head)——压缩历史
# 在合并特性分支之前，如果发现已提交的内容中有些许拼写错误等
# 不妨提交一个修改，然后将这个修改包含到前一个提交之中，压缩成一个历史记录

# git remote add——本地仓库添加到远程仓库
# 在 GitHub 上创建的仓库路径为“git@github.com:用户名 /git-tutorial.git”
# git remote add origin git@github.com:github-book/git-tutorial.git
# 按照上述格式执行 git remote add命令之后，
# Git 会自动将git@github.com:github-book/git-tutorial.git远程仓库的名称设置为 origin（标识符）

# git push——推送至远程仓库
# git push -u origin master(分支名)
# u参数可以在推送的同时，将origin仓库的master分支设置为本地仓库当前分支的 upstream（上游）。
# 添加了这个参数，将来运行 git pull命令从远程仓库获取内容时，本地仓库的这个分支就可直接从 origin 的 master 分支获取内容，省去了另外添加参数的麻烦

# git clone——获取远程仓库
# git clone git@github.com:github-book/git-tutorial.git
# 执行 git clone命令后我们会默认处于 master 分支下，同时系统会自动将 origin 设置成该远程仓库的标识符
# 也就是说，当前本地仓库的 master 分支与 GitHub 端远程仓库（origin）的 master 分支在内容上是完全相同的

# 获取远程的 feature - D 分支
# git checkout -b feature-D origin/feature-D
# -b 参数的后面是本地仓库中新建分支的名称,新建分支名称后面是获取来源的分支名称

# git pull——获取最新的远程仓库分支
# git pull origin feature-D




