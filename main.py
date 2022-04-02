import time
import route.wrapper
import os.path

def main():
    CRED_PATH = 'data/user_credentials.csv'
    if not os.path.exists(CRED_PATH):
        with open(CRED_PATH, 'w') as f:
            f.write('S.n,Alias,Email,Password,Recovery Key')
    while True:
        print("###########################################################################")
        print("###  ####  ###   ####      #####   ########################################")
        print("### # ## # ## ### ##  ####  ### ### #######################################")
        print("### ##  ## ## ###### ###### ##  ###  ######################################")
        print("### ###### ##    ### ##   ####       ####### #   ###     ##################")
        print("### ###### ## ###### ##    ### ##### #######  ### ##### ###################")
        print("### ###### ## ### ##  ## # ### ##### ##   ## #### #### ####################")
        print("#### #### ####   ####    #  ## ##### ##   ## #### ##     ##################")
        print("###########################################################################")

        print("[*] Choose Mega Account your Account :")
        print("[1] Accounts")
        print("[2] Add Account")
        print("[3] Download from Link (Quick Action)")
        print("[4] Quit")
        print("Choose an Option")
        
        try:
            choice = int(input(">>"))
            if (choice > 0 and choice < 5):
                route.wrapper.route_from(choice, CRED_PATH)
                break
            else:
                print("Please choose an option between 1-4")

        except ValueError:
            print("Please enter an integer value leading the option (1-4)")
            
        finally:
            time.sleep(2)
            continue

if __name__ == "__main__":
    main()
        