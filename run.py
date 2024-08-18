#!/home/newton/bin/miniconda3/bin/python

from utils.get_address import find_interface_in_network
from BitSrunLogin.LoginManager import LoginManager

lm = LoginManager()
ip_info = find_interface_in_network()
try:
    for interface, ip_address in ip_info.items():
        print(ip_address)
        lm.login(
            username = "liupeng19@mails.ucas.edu.cn",
            password = "7kiQf57bdVNVXN",
            ip = ip_address
        )
except Exception as e:
    print(f"Error dealing with IP-Interface group: {ip_info}, {e}")
