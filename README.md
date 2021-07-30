fork自：https://github.com/coffeehat/BIT-srun-login-script

# 概述

中国科学院大学于2021年中更换为深澜校园网认证系统。

寻找解决方案时发现了上述项目，稍作修改适应国科大的系统环境，并增加了远程登录的功能（只需要知道对方的IP就可以）。

从此想给谁登录就给谁登录，再也不用担心没有界面了\≥▽≤/~


具体细节请参考前作：[深澜校园网登录的分析与python实现-北京理工大学版](https://zhuanlan.zhihu.com/p/122556315)

# 文件说明

|文件|说明|
|:-:|:-:|
|BitSrunLogin/|深澜登录函数包|
|login_demo.py|登录示例脚本|
|always_online.py|在线监测脚本，如果监测到掉线则自动重连|

always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py &
```
