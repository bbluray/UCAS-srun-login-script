import subprocess
import ipaddress
import logging
from get_os import get_os


def parse_windows_output(stdout, networks):
    interfaces = {}
    current_interface = None
    for line in stdout.splitlines():
        if "适配器" in line:
            current_interface = line.split(":")[0].strip()
        elif 'IPv4 地址' in line:
            ip_addr = line.split(":")[1].strip()
            for n in networks:
                if ipaddress.ip_address(ip_addr) in n:
                    interfaces[current_interface] = ip_addr
    return interfaces


def parse_linux_output(stdout, networks):
    interfaces = {}
    current_interface = None
    for line in stdout.splitlines():
        if line.startswith(' '):
            if 'inet ' in line:
                ip_info = line.split()
                ip_addr = ip_info[1].split('/')[0]
                for n in networks:
                    if ipaddress.ip_address(ip_addr) in n:
                        interfaces[current_interface] = ip_addr
        else:
            if line:
                current_interface = line.split(': ')[1].split('@')[0]
    return interfaces


def find_interface_in_network(ucas_networks=["124.16.70.0/23", "124.16.111.0/24"]):
    """
    LoginManager 的 always_online.py 默认使用 SRUN 界面的返回解析作为登录地址，
    这并不符合我们的要求，因为我们希望：
    * 每一台机器都接入校园网
    * 每一台机器都可以通过校园网被外网访问，尽管这有些危险
    因此，需要通过本地查询获取接口 IP 地址。

    :param network_address: 校园网的网段地址，国科大学园二的地址是 `124.16.70.0/23` 和 `124.16.111.0/24`.
    """
    networks = [ipaddress.ip_network(n) for n in ucas_networks]
    os_type = get_os()

    cmd_map = {
        "windows": ['ipconfig'],
        "macos": ["ifconfig"],
        "debian": ['ip', 'address'],
        "openwrt": ['ip', 'address']
    }

    if os_type not in cmd_map:
        raise ValueError("Unsupported OS")

    result = subprocess.run(
        cmd_map[os_type], stdout=subprocess.PIPE, text=True)

    if os_type == "windows":
        return parse_windows_output(result.stdout, networks)
    elif os_type in ("debian", "openwrt"):
        return parse_linux_output(result.stdout, networks)
    else:
        raise ValueError("Unsupported OS")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        matching_interfaces = find_interface_in_network()
        print(matching_interfaces)
    except Exception as e:
        logging.error(e)
