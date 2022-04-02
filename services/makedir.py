import os
from route.actions import Action


def makeDir(email, password):
    NEW_PATH = str(input("Enter the new path you want to create: "))
    os.system("megatools mkdir -u {} -p {} \"/Root/{}\"".format(email, password, NEW_PATH))
    Action()