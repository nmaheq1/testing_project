import mysql.connector
from tkinter import messagebox
import Accounts as accounts
class DataBase():
    # creates a class called database
    # creates database tables

    def __init__(self):
        db = self.connectDB()
        mycursor = db.cursor()

        #create the user table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Accounts(
                AccountsID TEXT NOT NULL,
                Username VARCHAR(32) NOT NULL,
                Password VARCHAR(32) NOT NULL,
                PRIMARY KEY(AccountsID)
                );''')
        #create table for students
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Students
                StudID TEXT NOT NULL,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                PRIMARY KEY(StudID)
                Foreign KEY(AccountsID)
                );''')

        #create table for test details
        mycursor.execute('''CREATE TABLE IF NOT EXISTS TestDetails(
                TestID INT NOT NULL,
                Date DATE NOT NULL,
                Skills TEXT NOT NULL,
                Score TINYINT NOT NULL,
                Feedback TEXT NOT NULL,
                PRIMARY KEY(TestID)
                Foreign KEY(StudID)
                );''')
        #creates table for skills
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Skills(
                SkillsID INT AUTO_INCREMENT NOT NULL,
                MaxScore TINYINT NOT NULL,
                Rating TINYINT NOT NULL,
                PRIMARY KEY(SkillsID)
                );''')

        #commit the changes
        db.commit()
        #close connection
        db.close()
        return

    def connectDB(self):
        try:
            db = mysql.connector.connect(
                host="www.db4free.net",
                user="maheqn",
                password="specialkit456",
                database="*******"
            )
            return db
        except:
            messagebox.showerror("cannot connect")
            return 1

    def saveUser(self,data):
        accountID = data [0][0]
        print(accountID)
        username = data [0][1]
        password = data [0][2]
        currentUser.setAccountID(accountID)
        currentUser.setUsername(username)
        currentuser.setPassword(password)
        return

    def saveAccount(self,username,password):
        try:
            #create connection
            db = self.connectDB()
            mycursor = db.cursor()
            mycursor.execute('''INSERT INTO Accounts(Username,Password)
    VALUES (%s,%s)''',
                             (username,password))
            #commit chnages to database
            db.commit()
            #close connection
            db.close()
        except:
            messagebox.showerror("database error")
            return 1
        return 0

    # Function takes email, username and password as parameters
    # Function checks these against the database
    # Returns results
    # Returns 1 if failed
    def DB_login(self, username, password):
        try:
            # Creates connection to database
            db = self.connectDB()
            mycursor = db.cursor()
            mycursor.execute('''SELECT * FROM Accounts WHERE Username = %s AND 
    password = %s''', (username, password))
            results = mycursor.fetchall()
            if len(results) > 0:
                self.saveUser(results)
            # Close connection
            db.close()
            return results
        except:
            messagebox.showerror("Database Error")
            return 1

    def saveTestDetails(self,testInfo,studentName):
        #connects to database
        db = self.connectDB()
        mycursor = db.cursor()

        #stores each element of testInfo in separate variables
        date = testInfo[0].get()
        skills = testInfo[1].get()
        score = int(testInfo[2].get())
        feedback = testInfo[3].get()

        #uses findStudID method to find primary key of corresponding student
        studID = self.findStudID(studentName)

        try:
            # Executes query
            mycursor.execute('''INSERT INTO TestDetails(Date,Skills,Score,Feedback, 
            StudID)
             VALUES (%s,%s,%s,%s)''', (date, skills,
                                       score, feedback,studID))
            db.commit()  # Commits the changes to database
            db.close()  # Closes connection to database
            return 0
        except:
            messagebox.showerror('Error', 'Database Error')
            db.close()
            return 1
