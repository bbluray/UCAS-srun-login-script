# 确保文件存在
TARGET="/usr/local/bin/auto_login"
sudo git clone https://github.com/LittleNewton/UCAS-srun-login-script.git ${TARGET}

# 确保权限正确
sudo chmod +x ${TARGET}/run.py

# 拷贝 systemd 服务和定时器配置文件
sudo cp ${TARGET}/systemd/ucas-login.service /etc/systemd/system/
sudo cp ${TARGET}/systemd/ucas-login.timer /etc/systemd/system/

# 重载服务
sudo systemctl daemon-reload
sudo systemctl enable ucas-login.timer
sudo systemctl start ucas-login.timer
sudo journalctl -xeu ucas-login
