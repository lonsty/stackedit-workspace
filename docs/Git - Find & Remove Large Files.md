想象一下这样的情景

- `Git` 提交时，你忘记把 `venv`、`dist` 、一些大文件或无关文件加入 `.gitignore`，就推上了仓库
- 团队开发时，你的好队友推上去一堆杂七杂八的文件

实际上整个仓库只统计代码的话，顶多几 MB 大小，但因为各种原因，却变成了几百 MB 上 GB 的大胖子。你以为只需要在下次提交时，把那些无关的文件删除就能瘦身？

Git 仓库位于项目根目录的 `.git` 文件夹，其中保存了从仓库建立（`git init` ）以来所有的代码增删。 每一个提交（Commit）相当于一个Patch应用在之前的项目上，借此一个项目可以回到任何一次提交时的文件状态。

于是在 Git 中删除一个文件时，Git 只是记录了该删除操作，该记录作为一个Patch存储在 `.git` 中。 删除前的文件仍然在 Git 仓库中保存着。直接删除文件并提交起不到给 Git 仓库瘦身的效果。

在 Git 仓库彻底删除一个文件只有一种办法：重写（Rewrite）涉及该文件的所有提交。手动删除那不得累死，好在有工具可以使用。

## 首先找出历史提交中的所有文件
## Find large objects in git history

> https://stackoverflow.com/a/42544963/11377288

#### List all blob objects in the repository, sorted from smallest to largest.
```
git rev-list --objects --all \
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| sed -n 's/^blob //p' \
| sort --numeric-sort --key=2 \
| cut -c 1-12,41- \
| $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```

#### To exclude files that are present in  `HEAD`
```
git rev-list --objects --all \
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| sed -n 's/^blob //p' \
| grep -vF --file=<(git ls-tree -r HEAD | awk '{print $3}') \
| sort --numeric-sort --key=2 \
| cut -c 1-12,41- \
| $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```

#### To  show only files exceeding given size  (e.g. 1 MiB = 220 B)
```
git rev-list --objects --all \
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| sed -n 's/^blob //p' \
| awk '$2 >= 2^20' \
| sort --numeric-sort --key=2 \
| cut -c 1-12,41- \
| $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```

## 然后剔除不想保留的文件（夹），并将整理后的仓库提交
## BFG Repo-Cleaner

> [https://rtyley.github.io/bfg-repo-cleaner/](https://rtyley.github.io/bfg-repo-cleaner/)

### Usage

First clone a fresh copy of your repo, using the  [`--mirror`](http://stackoverflow.com/q/3959924/438886)  flag:

```
$ git clone --mirror git://example.com/some-big-repo.git
``` 

This is a  [bare](http://git-scm.com/docs/gitglossary.html#def_bare_repository)  repo, which means your normal files won't be visible, but it is a  _full_  copy of the Git database of your repository, and at this point you should  **make a backup of it**  to ensure you don't lose anything.

Now you can run the BFG to clean your repository up:

```
$ java -jar [bfg.jar](https://rtyley.github.io/bfg-repo-cleaner/#download) --strip-blobs-bigger-than 100M some-big-repo.git
``` 

The BFG will update your commits and all branches and tags so they are clean, but it doesn't physically delete the unwanted stuff. Examine the repo to make sure your history has been updated, and then use the standard  [`git gc`](http://git-scm.com/docs/git-gc)  command to strip out the unwanted dirty data, which Git will now recognise as surplus to requirements:

```
$ cd some-big-repo.git
$ git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

Finally, once you're happy with the updated state of your repo, push it back up  _(note that because your clone command used the  `--mirror`  flag, this push will update  **all**  refs on your remote server)_:

```
$ git push
```

At this point, you're ready for everyone to ditch their old copies of the repo and do fresh clones of the nice, new pristine data. It's best to delete all old clones, as they'll have dirty history that you  _don't_  want to risk pushing back into your newly cleaned repo.

### Examples

In all these examples  `bfg`  is an alias for  `java -jar bfg.jar`.

Delete all files named 'id_rsa' or 'id_dsa' :

```
$ bfg **--delete-files id_{dsa,rsa}**  my-repo.git
```

Remove all blobs bigger than 50 megabytes :

```
$ bfg **--strip-blobs-bigger-than 50M**  my-repo.git
```

Replace all passwords listed in a file  _(prefix lines 'regex:' or 'glob:' if required)_  with  `***REMOVED***`  wherever they occur in your repository :

```
$ bfg **--replace-text passwords.txt**  my-repo.git
```

Remove all folders or files named '.git' - a  [reserved filename](https://github.com/git/git/blob/d29e9c89d/fsck.c#L228-L229)  in Git. These often  [become a problem](http://stackoverflow.com/q/16821649/438886)  when migrating to Git from other source-control systems like Mercurial :

```
$ bfg **--delete-folders .git --delete-files .git  --no-blob-protection**  my-repo.git
```

For further command-line options, you can run the BFG without any arguments, which will output  [text like this](https://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=com.madgag&a=bfg&v=LATEST&e=txt).

以上操作可以为仓库瘦身，但是因为被删除文件之后的所有 commit 都被重写了，相关的那些 tag 也会一并消失。所以最好的是在每次提交时，检查清楚哪些内容应该提交到仓库。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjE5Njg1OV19
-->