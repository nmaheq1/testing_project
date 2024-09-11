import SQLdatabase

class User():
    # Initialises class with attributes to store key data for the account
    def __init__(self):
        self.accountID = ''
        self.username = ''
        self.password = ''

    # Method to get user's accountID
    def getAccountID(self):
        return self.accountID

    # Method to set the user's accountID
    def setAccountID(self, givenAccountID):
        self.accountID = givenAccountID
        return

    # Method to change username for the user's account
    def setUsername(self, givenUsername):
        self.username = givenUsername
        return

    # Method to get the user's username
    def getUsername(self):
        return self.username

    # Method to get user's password
    def getPassword(self):
        return self.password

    # Method to change user's password
    def setPassword(self, givenPassword):
        self.password = givenPassword
        return