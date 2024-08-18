import subprocess
import ipaddress
import platform


def find_interface_in_network(ucas_networks=["124.16.70.0/23", "124.16.111.0/24"]):
    """
        LoginManager 的 always_online.py 默认使用 SRUN 界面的返回解析作为登录地址，
        这并不符合我们的要求，因为我们希望：
        * 每一台机器都接入校园网
        * 每一台机器都可以通过校园网被外网访问，尽管这有些危险
        因此，需要通过本地查询获取接口 IP 地址。

        :param network_address: 校园网的网段地址，国科大学园二的地址是 `124.16.70.0/23` 和 `124.16.111.0/24`.
    """
    # 创建网络对象
    networks = [ipaddress.ip_network(n) for n in ucas_networks]

    # 检查操作系统
    os_type = platform.system()
    if os_type == "Windows":
        cmd = ['ipconfig']
    elif os_type == "Darwin":
        return
    elif os_type == "Linux":
        cmd = ['ip', 'address']
    else:
        print("system not support")
        return

    # 执行命令
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    # 初始化变量
    interfaces = {}
    current_interface = None

    # 根据操作系统解析命令输出
    if os_type == "Windows":
        # 解析 'ipconfig' 输出
        for line in result.stdout.splitlines():
            if "适配器" in line:
                current_interface = line.split(":")[0].strip()
            elif 'IPv4 地址' in line:
                ip_addr = line.split(":")[1].strip()
                for n in networks:
                    if ipaddress.ip_address(ip_addr) in n:
                        interfaces[current_interface] = ip_addr
    elif os_type == "Linux":
        # 解析 'ip addr' 输出
        for line in result.stdout.splitlines():
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


if __name__ == "__main__":
    # 执行函数并打印结果
    matching_interfaces = find_interface_in_network()
    print(matching_interfaces)
