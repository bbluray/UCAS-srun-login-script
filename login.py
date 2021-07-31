from BitSrunLogin.LoginManager import LoginManager
import sys

lm = LoginManager()
if(len(sys.argv)<3 or len(sys.argv)>4):
    print("argv len err")
if(len(sys.argv)==3):
    lm.login(
    username = sys.argv[1],
    password = sys.argv[2],
    )
if(len(sys.argv)==4):
    lm.login(
        username = sys.argv[1],
        password = sys.argv[2],
        ip = sys.argv[3]
    )
