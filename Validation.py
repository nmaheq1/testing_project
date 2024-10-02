import SQLdatabase as DB
import datetime
import hashlib

class validation():
    def __init__(self):
        self.DB = DB.Database()
        return

    def checkUsername(self,givenUsername):
        lenValid=False
        usernames = self.DB.getUsername()
        if len(givenUsername)>3 and len(givenUsername) < 17:
            lenValid = True
        for username in usernames:
            if username == self.hash(givenUsername):
                return 1, "Username already exists"

        # If the length of the username is invalid an error message is returned
        if lenValid == False:
            return 1, "Username must be between 3 and 17 characters"  # returns boolean value and error message
        return 0, "no error"  # returns boolean value and error message

        # Function to validate password
        # Takes password to be validated as a parameter
        # Returns a boolean value based on if password is valid

    def checkPassword(self, password):
        errorMessage = ''
        hasUppercase = False
        hasLowercase = False
        hasNumber = False
        # Checks password is within character limits
        if len(password) >= 8 and len(password) < 17:
            #Searches for uppercase letters, lowercase letters and numbers
            for char in password:
                asciiValue = ord(char)
                if asciiValue >= 65 and asciiValue <= 90:
                    hasUppercase = True
                else:
                    errorMessage = "Passsword must contain an Uppercase letter" # Sets appropriate error message
                if asciiValue >= 97 and asciiValue <= 122:
                    hasLowercase = True


                    errorMessage = "Password must contain a lowercase letter"
     # Sets appropriate error message
                if asciiValue >= 48 and asciiValue <= 57:
                    hasNumber = True
                    errorMessage = "Password must contain a number"  # Sets appropriate error message
            else:
                errorMessage = "Password must be between 8 and 17 characters"  # Sets appropriat error message
    # Returns if all conditions are met
            if hasUppercase and hasLowercase and hasNumber:
                return 0, "no error"  # returns boolean value and error message
    # Returns if conditions aren't met
            else:
                return 1, errorMessage  # returns boolean value and error message


# Checks if any fields have been left blank
def checkEntries(self, entries):
    for entry in entries:
        entry = entry.get()
        entry = entry.strip()
        if len(entry) == 0:
            return 1
    return 0



