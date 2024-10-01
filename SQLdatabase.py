import mysql.connector
from tkinter import messagebox

class DataBase():
    # Initializes the database and creates tables
    def __init__(self):
        db = self.connectDB()
        if db == 1:
            return  # Exit if connection failed
        mycursor = db.cursor()

        # Create the Accounts table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Accounts(
                AccountsID VARCHAR(36) NOT NULL,
                Username VARCHAR(32) NOT NULL,
                Password VARCHAR(32) NOT NULL,
                PRIMARY KEY (AccountsID)
                );''')

        # Create the Students table with a proper foreign key referencing Accounts table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Students(
                StudID VARCHAR(36) NOT NULL,
                FirstName VARCHAR(50) NOT NULL,
                LastName VARCHAR(50) NOT NULL,
                AccountsID VARCHAR(36),  -- Foreign key column
                PRIMARY KEY (StudID),
                FOREIGN KEY (AccountsID) REFERENCES Accounts(AccountsID) ON DELETE CASCADE ON UPDATE CASCADE
                );''')

        # Create the TestDetails table with a foreign key referencing the Students table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS TestDetails(
                TestID INT AUTO_INCREMENT NOT NULL,
                Date DATE NOT NULL,
                Skills TEXT NOT NULL,
                Score TINYINT NOT NULL,
                Feedback TEXT NOT NULL,
                StudID VARCHAR(36),  -- Foreign key column
                PRIMARY KEY (TestID),
                FOREIGN KEY (StudID) REFERENCES Students(StudID) ON DELETE CASCADE ON UPDATE CASCADE
                );''')

        # Create the Skills table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS Skills(
                SkillsID INT AUTO_INCREMENT NOT NULL,
                MaxScore TINYINT NOT NULL,
                Rating TINYINT NOT NULL,
                PRIMARY KEY (SkillsID)
                );''')

        # Commit the changes
        db.commit()

        # Close the connection
        db.close()

    def connectDB(self):
        try:
            db = mysql.connector.connect(
                host="www.db4free.net",
                user="maheqnas",
                password="kamkamkam",
                database="khgjkl"
            )
            return db
        except mysql.connector.Error as e:
            messagebox.showerror("Connection Error", f"Cannot connect to the database. Error: {str(e)}")
            return 1


