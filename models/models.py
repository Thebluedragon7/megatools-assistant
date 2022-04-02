class User:
    def __init__(self, username, email, password, recoverykey):
        self.username = username
        self.email = email
        self.password = password
        self.recoverykey = recoverykey
        
    def __str__(self):
        return self.username