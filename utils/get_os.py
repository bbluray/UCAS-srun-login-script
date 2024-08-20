import platform
import os
import re
import logging


def read_os_release():
    try:
        with open('/etc/os-release') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("'/etc/os-release' file not found.")
        raise


def detect_linux_distribution(os_release):
    distributions = {
        "debian": "Debian GNU/Linux",
        "openwrt": "OpenWrt"
    }
    for key, value in distributions.items():
        if value in os_release:
            return key
    logging.error("Unsupported Linux distribution.")
    raise ValueError("Unsupported Linux distribution.")


def get_os():
    os_type = platform.system()
    if os_type == "Windows":
        return "windows"
    elif os_type == "Darwin":
        return "macos"
    elif os_type == "Linux":
        os_release = read_os_release()
        return detect_linux_distribution(os_release)
    else:
        logging.error("Unsupported OS: {}".format(os_type))
        raise ValueError("Unsupported OS")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print(get_os())
    except Exception as e:
        logging.error(e)
