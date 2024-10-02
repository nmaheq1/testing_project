class User:
    # Initializes class with attributes to store key data for the account
    def __init__(self):
        self.studID = ''
        self.password = ''
        self.firstName = ''
        self.lastName = ''
        self.email = ''
        self.phoneNumber = ''

    # Getters and Setters for studID
    def getStudID(self):
        return self.studID

    def setStudID(self, givenStudID):
        self.studID = givenStudID

    # Getters and Setters for password
    def getPassword(self):
        return self.password

    def setPassword(self, givenPassword):
        self.password = givenPassword

    # Getters and Setters for firstName
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, givenFirstName):
        self.firstName = givenFirstName

    # Getters and Setters for lastName
    def getLastName(self):
        return self.lastName

    def setLastName(self, givenLastName):
        self.lastName = givenLastName

    # Getters and Setters for email
    def getEmail(self):
        return self.email

    def setEmail(self, givenEmail):
        self.email = givenEmail

    # Getters and Setters for phoneNumber
    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, givenPhoneNumber):
        self.phoneNumber = givenPhoneNumber
