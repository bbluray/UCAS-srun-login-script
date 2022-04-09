fork自：https://github.com/coffeehat/BIT-srun-login-script

增加了登出
增加了远程登录的功能（只需要知道对方的IP就可以）。

# 概述

国科大深澜校园网登录python脚本，可用于支持python的网络设备，给任意校园网内的设备登录上网账号。

（已验证可以从学园二登录西区宿舍）

具体细节请参考前作：[深澜校园网登录的分析与python实现-北京理工大学版](https://zhuanlan.zhihu.com/p/122556315)

# 文件说明

|文件|说明|
|:-:|:-:|
|BitSrunLogin/|深澜登录函数包|
|login.py|使用参数登录|
|login_demo.py|登录示例脚本|
|always_online.py|在线监测脚本，如果监测到掉线则自动重连|

login.py后面跟参数使用，分别是`账号`，`密码`，`远程ip`：
``` bash
python login.py [account] [password] [ip]
```

always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py &
```
