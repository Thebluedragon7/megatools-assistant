import os
from route.actions import Action

def upload(email, password):
    LOCAL_LOC = '../sync/'
    REMOTE_LOC = str(input("Enter the remote location where you want to upload: "))
    os.system("megatools copy -u {} -p {} --local {} --remote \"/Root/{}\"".format(email, password, LOCAL_LOC, REMOTE_LOC))
    Action()