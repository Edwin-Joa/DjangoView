1. 从github克隆git项目：
   * 命令：git clone 链接地址
2. 下载好项目后，进入项目目录，首先要设定身份：
   * git config user.name '名字'
   * git config user.email '邮箱'
3. 设定好身份之后即可对文件进行编辑了
4. 对某文件编辑后，设置文件追踪
   * git add .   ——自动追踪所有编辑的文件,将文件放至本地暂存区
5. 编辑完成后，将所有追踪后的文件提交至本地仓库区
   * git commit -m '备注内容'
6. 提交至本地仓库后，若完成了本次编辑，可以将本地库中的项目同步至github
   * git push



以上为git的基本操作，在编辑过程中，其他操作：

1. 查看当前git状态：git status
2. 查看本机编辑日志：git log
3. 查看编辑日志、版本号：git refconfig

