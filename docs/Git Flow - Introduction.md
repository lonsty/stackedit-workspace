# Git Flow

原文：[https://gitbook.tw/chapters/gitflow/why-need-git-flow.html](https://gitbook.tw/chapters/gitflow/why-need-git-flow.html)

當在同一個專案一起開發的人數越來越多，如果沒有訂好規矩，每個人的 Commit 習慣可能都不同，放任大家隨便 Commit 的話遲早會造成災難。

在 2010 年的時候，就有人提出了一套流程，或說是訂了一套規矩讓大家可以遵守：

網址：[http://nvie.com/posts/a-successful-git-branching-model/](http://nvie.com/posts/a-successful-git-branching-model/)

不過因為這套流程是 2010 年提出的，到現在也已經九年了，這幾年來也陸續有其它優秀的開發流程，例如 GitHub Flow、Gitlab Flow 等流程，我們這邊僅以 Git Flow 做為介紹。

## 分支應用情境

根據 Git Flow 的建議，主要的分支有  `master`、`develop`、`hotfix`、`release`  以及  `feature`  這五種分支，各種分支負責不同的功能。其中 Master 以及 Develop 這兩個分支又被稱做長期分支，因為他們會一直存活在整個 Git Flow 裡，而其它的分支大多會因任務結束而被刪除。

![git flow](https://gitbook.tw/images/tw/gitflow/why-need-git-flow/flow.png)

### Master 分支

主要是用來放穩定、隨時可上線的版本。這個分支的來源只能從別的分支合併過來，開發者不會直接 Commit 到這個分支。因為是穩定版本，所以通常也會在這個分支上的 Commit 上打上版本號標籤。

### Develop 分支

這個分支主要是所有開發的基礎分支，當要新增功能的時候，所有的 Feature 分支都是從這個分支切出去的。而 Feature 分支的功能完成後，也都會合併回來這個分支。

### Hotfix 分支

當線上產品發生緊急問題的時候，會從 Master 分支開一個 Hotfix 分支出來進行修復，Hotfix 分支修復完成之後，會合併回 Master 分支，也同時會合併一份到 Develop 分支。

為什麼要合併回 Develop 分支？如果不這麼做，等到時候 Develop 分支完成並且合併回 Master 分支的時候，那個問題就又再次出現了。

那為什麼一開始不從 Develop 分支切出來修？因為 Develop 分支的功能可能尚在開發中，這時候硬是要從這裡切出去修再合併回 Master 分支，只會造成更大的災難。

### Release 分支

當認為 Develop 分支夠成熟了，就可以把 Develop 分支合併到 Release 分支，在這邊進行算是上線前的最後測試。測試完成後，Release 分支將會同時合併到 Master 以及 Develop 這兩個分支上。Master 分支是上線版本，而合併回 Develop 分支的目的，是因為可能在 Release 分支上還會測到並修正一些問題，所以需要跟 Develop 分支同步，免得之後的版本又再度出現同樣的問題。

### Feature 分支

當要開始新增功能的時候，就是使用 Feature 分支的時候了。Feature 分支都是從 Develop 分支來的，完成之後會再併回 Develop 分支。
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIxNzA4MDM4Nl19
-->