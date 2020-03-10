- 进入安装包路径在`Finder`中，使用快捷键：`command + Shift +G`  
### for example，寻找python的安装路径：
* 首先在homebrew查看安装python的库的存放位置路径：site-packages。  
* 在`Mac`终端`cd`到对于路径：`$(brew --prefix)/lib/pythonX.Y/site-packages`查看python对应的版本。
* `echo $(brew --prefix)/lib/python3.7/site-package`  在终端打印在mac上python库所对应的详细位置。
* 最后在`Finder`中，使用快捷键：`command + Shift +G`调出去对应位置的快捷框输入即可。

### Mac 配置环境变量的方法
source .bash_profile  //更新环境变量配置，使新设置的环境变量生效
* vi .bash_profile 
* 由于Mac公司启用了`.zshrc`所以`.bash_profile`配置将不在起作用。
* 以后配置环境变量需要去Mac的家目录下`ls -a`,然后`vi .zshrc`即可。
