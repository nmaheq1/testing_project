# Imports hashlib library to hash data
import hashlib
# Imports tkinter library to create graphical user interface
from tkinter import *
from tkinter import messagebox
# Imports UIWindow.py module to allow for a consistent and customisable UI
import UIWindow as UI
# Imports myDatabase.py module to allow the login system to access the database
import SQLdatabase as DB
# Imports Validation.py module to allow the login system to validate inputs and data
import Validation as valid

class loginSystem():
    def __init__(self, database, Validation):
        self.formColour = '#EEEAEA'
        self.fontColour = '#000000'
        self.font = 'Serif'
        self.DB = database
        self.valid = Validation
        self.welcomeScreen()
        return
# Function in loginSystem class
# Creates welcome page
    def welcomeScreen(self):
        win1 = UI.Window('Welcome Screen', 450, 300, self.formColour, self.fontColour, self.font)
        win1.centreWindow()
        headerFrame = win1.getHeader()
        bodyFrame = win1.getBody()

        win1.showTitle(100)
        titleLabel = win1.customLabel('header', 'Welcome Page', 10)
        titleLabel.grid(row=1, column=1, padx=100)

        # Replace the login and sign-up labels and buttons with Student and Teacher login
        studentLabel = win1.customLabel('body', 'Student Login:', 10)
        studentLabel.grid(row=0, column=1, padx=140, pady=10)
        studentButton = Button(bodyFrame, text="Student Login", command=lambda: [win1.destroyWindow(), self.studentLoginScreen()])
        studentButton.grid(row=1, column=1, padx=140, pady=10)
        studentButton['bg'] = win1.getColour()
        studentButton['font'] = (self.font, 10)

        teacherLabel = win1.customLabel('body', 'Teacher Login:', 10)
        teacherLabel.grid(row=2, column=1, padx=140, pady=10)
        teacherButton = Button(bodyFrame, text="Teacher Login", command=lambda: [win1.destroyWindow(), self.teacherLoginScreen()])
        teacherButton.grid(row=3, column=1, padx=140, pady=10)
        teacherButton['bg'] = win1.getColour()
        teacherButton['font'] = (self.font, 10)

        win1.mainloop()
        return

    def studentLoginScreen(self):
        #creates a window using UI module and window class

    def signupScreen(self):
        win2 = UI.window("Sign Up",700,250,self.formColour,self.fontColour,self.font)
        win2.centreWindow()
        headerFrame = win2.getheader()
        bodyFrame = win2.getBody()
        win2.showTitle(170)

        titleLabel = win2.customLabel("header","Sign Up",10)
        titleLabel.grid(row=1,column=1)
        titleLabel["fg"]= "#747373"

        #labels toescrive entries
        labelList = ["Username:","Password: "]
        for i in range(2):
            tmp = win2.customLabel("body", labelList[i],10)
            tmp.grid(row =i,column=1,padx=10)
        Entries= []

        #entry fields to describe inputs needed

        usernameEntryField = Entry(bodyFrame)
        usernameEntryField.grid(row=0, column = 2)
        Entries.append(usernameEntryField)

        passwordEntryField = Entry(bodyFrame, show='*')
        passwordEntryField.grid(row=1, column=2)
        Entries.append(passwordEntryField)

        #button for input entry
        enterButton = Button(bodyFrame, text="Enter", command=lambda:
        self.signUp(Entries))
        enterButton.grid(row=4, column=3, pady=10, padx=20)
        enterButton['bg'] = win2.getColour()
        enterButton['font'] = (self.font, 10)

        #button to return to welcome page

        backButton = Button(bodyFrame, text="Back", command=lambda:
    [win2.destroyWindow(), self.welcomeScreen()])
        backButton.grid(row=4, column=0, pady=10, padx=20)
        backButton['bg'] = win2.getColour()
        backButton['font'] = (self.font, 10)

        win2.mainloop()
        return

    def signUp(self,entries):
        username = entries[0].get()
        password = entries[1].get()
        # Validates the users inputs using the validation class
        # Checks if all entries have been entered using validation class
        if self.valid.checkEntries(entries) == 0:
            usernameCheck = self.valid.checkUsername(username)
            passwordCheck = self.valid.checkPassword(password)

        # If username is invalid error message returned from validation
            if usernameCheck[0] == 1:
                messagebox.showerror("Error", usernameCheck[1])
                return
            # If password is invalid error message returned from validation function is shown
            if passwordCheck[0] == 1:
                messagebox.showerror("Error", passwordCheck[1])
                return
        #return error if entry is left blank
        else:
            messagebox.showerror("Error", "All fields must be entered")
            return
        # Hashes username and password before creating account
        hashUsername = self.hash(username)
        hashPassword = self.hash(password)

        # Adds account using database class
        addAccountSuccess = self.DB.saveAccount(hashUsername, hashPassword)

        #checks whether account creation was successful
        if addAccountSuccess == 0:
            messagebox.showinfo("Success", "Account Created")

        else:
            messagebox.showerror("Error", "Failed to Create Account")

        self.welcomeScreen()
        return


    def loginScreen(self):
        # Creates window using UI module and Window class
        win3 = UI.Window('Login Screen', 450, 300, self.formColour,
                         self.fontColour, self.font)
        win3.centreWindow()
        headerFrame = win3.getHeader()
        bodyFrame = win3.getBody()
        # Shows title
        win3.showTitle(100)
        titleLabel = win3.customLabel('header', 'Log In Page', 10)
        titleLabel.grid(row=1, column=1, padx=100)
        titleLabel['fg'] = '#747373'
        # Creates labels to describe entries
        labelList = ['Username:', 'Password:']
        for i in range(2):
            tmp = win3.customLabel('body', labelList[i], 10)
        tmp.grid(row=i, column=1, padx=10)
        Entries = []

        # Entry fields to describe inputs needed

        usernameEntryField = Entry(bodyFrame)
        usernameEntryField.grid(row=0, column=2)

        Entries.append(usernameEntryField)
        passwordEntryField = Entry(bodyFrame, show='*')
        passwordEntryField.grid(row=1, column=2)
        Entries.append(passwordEntryField)
        # Button to enter inputs
        enterButton = Button(bodyFrame, text="Enter", command=lambda:
        [self.login(Entries, win3), win3.destroyWindow()])
        enterButton.grid(row=3, column=3, pady=30)
        enterButton['bg'] = win3.getColour()
        enterButton['font'] = (self.font, 10)
        # Button to return to welcome page
        backButton = Button(bodyFrame, text="Back", command=lambda:
        [win3.destroyWindow(), self.welcomeScreen()])
        backButton.grid(row=3, column=0, pady=30)
        backButton['bg'] = win3.getColour()
        backButton['font'] = (self.font, 10)
        win3.mainloop()
        return
    # Function to take inputs and valid them before using Database class to search for user
    def login(self, entries, win):
        username = entries[0].get()
        password = entries[1].get()
        # Validates the users inputs using the validation class
        # Checks if all entries have been entered using validation class
        if self.valid.checkEntries(entries) == 0:
            hashUsername = self.hash(username)
            hashPassword = self.hash(password)
            # Uses database class to check for matching users
            results = self.DB.DB_login(hashUsername, hashPassword)
            # If no user is found an error is returned and the user is redirected to the welcome screen
        if len(results) == 0:
            messagebox.showerror("Error", "No user found")
            win.destroyWindow()
            self.welcomeScreen()
            return
        #IF anentry is leftblankan error is returned and the user is redirected to the welcome screen
        else:
            messagebox.showerror("Error", "All fields must be entered")
            win.destroyWindow()
            self.welcomeScreen()
        return
        # Shows successful login message
        messagebox.showinfo('Login', 'Successfully logged In')
        win.destroyWindow()
        return