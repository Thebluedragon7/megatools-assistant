import os
from route.actions import Action


def checkStatus(email, password: str):
    os.system("megatools df -h -u {} -p {}".format(email, password))
    Action()