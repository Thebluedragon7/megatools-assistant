import time
from route.wrapper import action_from


def Action(User):
    while True:
        print("[+] What do you want to do with {} Mega Account?".format(User.username))
        print("[0] Change Account")
        print("[1] View")
        print("[2] Upload")
        print("[3] Download")
        print("[4] Create Directory")
        print("[5] View Status")
        print("[6] get Link")


        try:
            choice = int(input(">>"))
            if (choice >= 0 and choice <= 6):
                action_from(choice, User.email, User.password)
                break
            else:
                print("Please choose an option between 1-6")

        except ValueError:
            print("Please enter an integer value leading the option (1-6)")
            
        finally:
            time.sleep(2)
            continue