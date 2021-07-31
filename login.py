from BitSrunLogin.LoginManager import LoginManager
import sys
print(sys.argv)

lm = LoginManager()
#NAS
lm.login(
    username = sys.argv[1],
    password = sys.argv[2],
    ip = sys.argv[3]
)
