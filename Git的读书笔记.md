

# Git的读书笔记



#### <u>**班级：20201441                      学号：2020144141                     姓名：李正国**</u>



#### 一、Git基本概念：

- Git是一套内容寻址文件系统
- .git的目录保存元数据和对象数据库的地方。克隆镜像仓库的时候，实际拷贝的就是该目录
- 从项目中取出某个版本的所以文件和目录，用以开始后续工作的叫做工程目录
- Git并不保存这些文件前后的差异数，而是保存每次更新时的文件快照

#### 二、Git工作流程：

- ##### 基本工作流程
  
   1.工作目录中修改某些文件
   2.对修改后的文件进行快照，然后保存到暂存区域
   3.提交更新，将文件快照永久转储到Git目录
   
- ##### git在本地实际上维护了“三棵树”：
  
   1.工作目录：持有实际文件
   2.缓存区（Index）：临时保存你的改动
   3.Head：最后一次提交后的结果
   
- ##### 、三棵树的流程：

   工作目录—>Idex—>Head

#### 三、简单命令

- 初始化项目\

```linux
git init
```

- 克隆项目

```linux
git clone [url]
```

- 检查当前文件状态

```linux
git status
```

- 跟踪新文件，或把已跟踪文件放到暂存区

```linux
git add [filename]
```

- 要查看尚未暂存的文件更新了哪些部分

```linux
git diff
```

- 查看已暂存文件和上次提交快照之间的差异

```linux
git diff -- cached
```

- 提交更新


```linux
git commit
或者
git commit -m '提交的说明注释'
```

- 跳过 git add 直接提交

```linux
git commit -a
```

- 移除文件

```linux
git rm [filename]
```

- 从Git仓库中删除，但仍保留在当前工作目录

```linux
git rm -- cached [filename]
```

- 移动文件

```linux
git mv [file_name_from] [file_name_to]
```

- 查看提交历史

```linux
git log
我们常用-p 选项展开显示每次提交的内容差异，用-2 则仅显示最近的两次更新：
git log -p -2
```

- 查看所有commit

```linux
git reflog
```

- 修改最后一次提交

```linux
git commit --amend
具体过程
git commit -m 'commit'                      第二次提交
git add [forgotten_file]                       修正第一个
git commit --amend
```

- 取消对文件修改

```linux
git checkout -- [filename]
```

- 查看远程仓库

```linux
git remote
git remote -v                     详细信息
```

- 添加远程仓库

```liunx
git remote add [you take a nickname] [url]
```

- 上传远程仓库

```linux
git push [remote_name] [branck_name]
如果在你推送数据前，已经有其他人推送若干更新，那你的推送将被驳回。
你必须先把它们的更新抓取到本地，合并到自己的项目中，才可以再次推送。
```

- 抓取数据

```linux
git fetch [remote_name]
```

- 创建标签

```linux
git tag -a [v1.4] -m 'my version 1.4'
```

- 列显已有标签

```linux
git tag
或者
git tag -l 'v1.4.2.*'
```

- 展示标签版本信息

```linux
git show [v1.4]
```

- 创建分支



```linux
git branch [name]
仅仅是建立一个新分支，不会自动切换到该分支中去
```

- 切换分支

```linux
git checkout [name]
```

- 删除分支

```linux
git branch -d [name]
```

- SSH生成公钥

```linux
ssh-keygen
```

- 整合远程再上传

```linux
git fetch origin
git merge orign/master
git push origin master
当修改代码后发现已经有人改动其他代码，需要先fetch再merge后才push
```

- 操作的url可以是本地路径，如

```linux
git clone /opt/git/project.git
或
git clone file://opt/git/project.git
```

- 回滚

```linux
git reset --hard <commit ID号>
参数的“hard”使工程目录都回滚，还有其他参数，现在还不会使用
```

#### 四、Git 的三种状态

##### 在 Git 内都只有三种状态：已提交（committed），已修改（modified）和已暂存（staged）。

- 已提交表示该文件已经被安全地保存在本地数据库中了；
- 已修改表示修改了某个文件，但还没有提交保存；
- 已暂存表示把已修改的文件放在下次提交时要保存的清单中。

#### 六、Git常用命令速查表![](C:\Users\白泽\Desktop\git.webp)