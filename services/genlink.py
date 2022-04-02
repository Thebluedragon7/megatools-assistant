import os
from route.actions import Action

def generateLink(email, password):
    EXPORT_PATH = str(input("Enter the file path to get public link: "))
    os.system("megatools export -u {} -p {} {}".format(email, password, EXPORT_PATH))
    Action()