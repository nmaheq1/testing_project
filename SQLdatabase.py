import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self):
        # Connect to the MySQL database
        self.connection = self.connect_db()

        if self.connection:
            # Create all tables
            self.create_tables()

    def connect_db(self):
        try:
            connection = mysql.connector.connect(
                host="www.db4free.net",
                user="maheqnas",  # replace with your username
                password="kamkamkam",  # replace with your password
                database="khgjkl"  # replace with your database name
            )
            if connection.is_connected():
                print("Successfully connected to the database")
            return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def create_tables(self):
        try:
            cursor = self.connection.cursor()

            # Create Students table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                StudID VARCHAR(36) NOT NULL, 
                FirstName VARCHAR(50) NOT NULL, 
                LastName VARCHAR(50) NOT NULL, 
                Email VARCHAR(100),
                PRIMARY KEY (StudID)
            );
            ''')

            # Create Assignments table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Assignments (
                AssignmentID INT AUTO_INCREMENT NOT NULL, 
                Title VARCHAR(100) NOT NULL, 
                Description TEXT, 
                DueDate DATE, 
                PRIMARY KEY (AssignmentID)
            );
            ''')

            # Create Skills table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Skills (
                SkillID INT AUTO_INCREMENT NOT NULL, 
                SkillName VARCHAR(100) NOT NULL, 
                MaxScore TINYINT NOT NULL, 
                PRIMARY KEY (SkillID)
            );
            ''')

            # Create AssignmentDetails table (linking Assignments and Skills)
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS AssignmentDetails (
                DetailID INT AUTO_INCREMENT NOT NULL, 
                AssignmentID INT NOT NULL, 
                SkillID INT NOT NULL, 
                StudID VARCHAR(36) NOT NULL, 
                ScoreObtained TINYINT NOT NULL, 
                PRIMARY KEY (DetailID),
                FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID) ON DELETE CASCADE ON UPDATE CASCADE, 
                FOREIGN KEY (SkillID) REFERENCES Skills(SkillID) ON DELETE CASCADE ON UPDATE CASCADE, 
                FOREIGN KEY (StudID) REFERENCES Students(StudID) ON DELETE CASCADE ON UPDATE CASCADE
            );
            ''')

            # Commit changes
            self.connection.commit()
            print("Tables created successfully.")

        except Error as e:
            print(f"Error while creating tables: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")

# Instantiate the DataBase class to create tables
db_instance = DataBase()
db_instance.close_connection()


