import subprocess
import ipaddress


def find_interface_in_network(network_address="124.16.70.0/23"):
    """
        LoginManager 的 always_online.py 默认使用 SRUN 界面的返回解析作为登录地址，
        这并不符合我们的要求，因为我们希望：
        * 每一台机器都接入校园网
        * 每一台机器都可以通过校园网被外网访问，尽管这有些危险
        因此，需要通过本地查询获取接口 IP 地址。

        :param network_address: 校园网的网段地址，国科大学园二的地址是 `124.16.70.0/23`.
    """
    # 创建网络对象
    network = ipaddress.ip_network(network_address)

    # 使用 'ip addr' 命令获取所有接口的 IP 配置
    result = subprocess.run(['ip', 'addr'], stdout=subprocess.PIPE, text=True)

    # 初始化变量
    current_interface = None
    interfaces = {}

    # 解析 'ip addr' 命令的输出
    for line in result.stdout.splitlines():
        if line.startswith(' '):
            if 'inet ' in line:
                ip_info = line.split()
                ip_addr = ip_info[1].split('/')[0]
                if ipaddress.ip_address(ip_addr) in network:
                    interfaces[current_interface] = ip_addr
        else:
            if line:
                current_interface = line.split(': ')[1].split('@')[0]

    return interfaces


if __name__ == "__main__":
    # 执行函数并打印结果
    matching_interfaces = find_interface_in_network()
    print(matching_interfaces)
