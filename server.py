from flask import Flask, request, jsonify, render_template 
from BitSrunLogin.LoginManager import LoginManager
import subprocess

app = Flask(__name__)

def run_login(username, password, ip_addr):
    # 将参数转换为字符串，并通过空格分隔
    args = ', '.join([f'"{username}"', f'"{password}"', f'"{ip_addr}"'])

    # 创建子进程，执行 login 函数
    process = subprocess.Popen(['python', '-c', f'import server; server.login({args})'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取子进程的标准输出和标准错误
    stdout, stderr = process.communicate()

    # 如果子进程返回了错误，抛出异常
    if process.returncode != 0:
        raise Exception(stderr.decode())

    # 返回子进程的标准输出
    return stdout.decode()

def login(username: str, password: str, ip_addr: str):
    lm = LoginManager()
    lm.login(username, password, ip_addr)
    return f"Login attempted for user: {username} from IP: {ip_addr}"

@app.route('/')
def return_default ():
    return render_template('index.html', message="")

@app.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    ip_addr  = data['ip_addr']

    result = run_login(username, password, ip_addr)
    return jsonify({"message": str(result)})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug=False)
