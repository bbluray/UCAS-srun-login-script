#!/bin/bash

# 确保文件存在
TARGET="/usr/local/bin/auto_login"
# 检查目标文件夹是否存在
if [ ! -d "$TARGET" ]; then
    # 文件夹不存在，克隆仓库到指定目录
    echo "Directory $TARGET does not exist. Cloning repository..."
    sudo git clone https://github.com/LittleNewton/UCAS-srun-login-script.git "$TARGET"
else
    # 文件夹存在，cd进入目录，执行git pull获取最新更新
    echo "Directory exists. Pulling latest updates..."
    cd "$TARGET"
    sudo git pull
fi

# 确保权限正确
sudo chmod +x ${TARGET}/run.py

# 拷贝 systemd 服务和定时器配置文件
sudo cp ${TARGET}/utils/linux_systemd/ucas-login.service /etc/systemd/system/
sudo cp ${TARGET}/utils/linux_systemd/ucas-login.timer /etc/systemd/system/

# 重载服务
sudo systemctl daemon-reload
sudo systemctl enable ucas-login.timer
sudo systemctl start ucas-login.timer
sudo journalctl -xeu ucas-login
