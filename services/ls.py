import os
from route.actions import Action

def ls(email, password):
    LOCATION = str(input("Enter the path to view: "))
    os.system("megatools ls -u {} -p {} \"/Root/{}\"".format(email, password, LOCATION))
    Action()