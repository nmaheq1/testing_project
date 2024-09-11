import Validation
import hashlib
from tkinter import messagebox
import UIWindow
import SQLdatabase
import studentMenu
import teacherMenu

def hash_input(inputvar):
    """
    Hashes the input string using SHA-256.
    """
    return hashlib.sha256(inputvar.encode('utf-8')).hexdigest()

def hashandfind(win, role, userVar, passVar):
    """
    Processes the login by validating the input, hashing the password,
    and directing the user to the appropriate menu based on their role.
    """
    # Validate the username and password
    if validation.validuser(userVar) and validation.validpass(passVar):
        passVar = hash_input(passVar)  # Hash the password

        # Determine the correct userID prefix based on the role
        if role.lower() == "student":
            userID = f"ST_{userVar}"
        elif role.lower() == "teacher":
            userID = f"TH_{userVar}"
        else:
            messagebox.showerror("Error", "Invalid role. Please restart the application.")
            win.destroy()
            loginUI.initial_window()
            return

        # Search the database for the user
        if SQLdatabase.searchUser(userID, passVar):
            messagebox.showinfo("Success", "Welcome to my app. You will now be directed to your menu.")
            win.destroy()  # Close the login window

            # Direct the user to the appropriate menu based on their role
            if role.lower() == "student":
                studentMenu.show_student_menu()  # Show the student menu
            elif role.lower() == "teacher":
                teacherMenu.show_teacher_menu()  # Show the teacher menu
        else:
            messagebox.showinfo("User not found",
                                "This account doesn't exist. Enter a different account or create a new one.")
            win.destroy()
            loginUI.initial_window()
    else:
        messagebox.showinfo("Invalid username or password",
                            "Password must be at least 8 characters. Username must be at least 4 characters.")
        win.destroy()
        loginUI.initial_window()

if __name__ == "__main__":
    pass

