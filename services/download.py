import os
from main import main
from route.actions import Action

def downloadFromLink(link):
    DOWNLOAD_LOCATION = '../downloads/'
    os.system("megatools dl --path \"{}\" \"{}\"".format(DOWNLOAD_LOCATION, link))
    main()

def download(email, password):
    REMOTE_LOCATION = str(input("Enter the remote location you want to download: "))
    DOWNLOAD_LOCATION = '../downloads/'
    os.system("megatools copy --download -u {} -p {} --local {} --remote \"/Root/{}\"".format(email, password, DOWNLOAD_LOCATION, REMOTE_LOCATION))
    Action()