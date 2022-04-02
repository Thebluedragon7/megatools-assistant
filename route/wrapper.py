from main import main
from services.download import download, downloadFromLink
from services.genlink import generateLink
from services.ls import ls
from services.makedir import makeDir
from services.status import checkStatus
from services.upload import upload
from services.user_handler import adduser, listuser



def route_from(choice: int, cred: str):
    match choice:
        case 1:
            listuser(cred)
        case 2:
            adduser(cred)
        case 3:
            link = str(input("Enter the link: "))
            downloadFromLink(link)
        case 4:
            exit()
        case _:
            pass

def action_from(choice: int, email: str, password: str):
    match choice:
        case 0:
            main()
        case 1:
            ls(email, password)
        case 2:
            upload(email, password)
        case 3:
            download(email, password)
        case 4:
            makeDir(email, password)
        case 5:
            checkStatus(email, password)
        case 6:
            generateLink(email, password)
        case _:
            pass