from asyncio import sleep
from main import main
import csv

def listuser(filename):
    
    rows = []
    
    with open(filename, 'r+') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    
        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
    
    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))
    
    #  printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')
    
    sleep(2)
    main.main()
    



def adduser(filename):
    with open(filename, 'a+') as csvfile:
        
        # collecting data from user
        username = str(input("Enter username: "))
        email = str(input("Enter email: "))
        password = str(input("Enter password: "))
        recoverykey = str(input("Enter recoverykey: "))
        
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        
        # writing the data rows
        csvwriter.writerows(
            [
                [username, email, password, recoverykey]
            ]
        )
        print("Successfully added new credential!")
        sleep(2)
        main.main()