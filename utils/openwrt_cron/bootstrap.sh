#!/bin/bash

TARGET="/root/auto_login"
# 检查目标文件夹是否存在
if [ ! -d "$TARGET" ]; then
    # 文件夹不存在，克隆仓库到指定目录
    echo "Directory $TARGET does not exist. Cloning repository..."
    git clone https://github.com/LittleNewton/UCAS-srun-login-script.git "$TARGET"
else
    # 文件夹存在，cd进入目录，执行git pull获取最新更新
    echo "Directory exists. Pulling latest updates..."
    cd "$TARGET"
    git pull
fi

# 设置源文件和目标文件路径
SOURCE_FILE="${TARGET}/utils/openwrt_cron/crontabs"
DESTINATION_FILE="/etc/crontabs/root"

# 检查源文件是否存在
if [ -f "$SOURCE_FILE" ]; then
    # 读取源文件内容并追加到目标文件中
    cat "$SOURCE_FILE" >>"$DESTINATION_FILE"
    echo "内容已追加到 $DESTINATION_FILE"
else
    echo "错误：源文件 $SOURCE_FILE 不存在。"
fi
