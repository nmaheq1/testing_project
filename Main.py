import datetime

from tkinter import *
from tkinter import messagebox
# Imports Login.py module to allow the login system to run before the main application.
import Login as Login
# Imports UIWindow.py module to allow for a consistent and customisable UI
import UIWindow as UI
# Imports myDatabase.py module to allow the application to access the database
import SQLdatabase as DB
# Imports Validation.py module to allow the application to validate inputs and data
import Validation as valid
# Imports pandas and pandastable modules to allow for dataframes and to be sued to store data
# Pandastable helps data to be neatly displayed in a table in the UI
import pandas as pd
from pandastable import Table, config
# Imports matplotlib library to plot data in graphs
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkA)

class App():
    # Constructor for class 'App'
    # Initiates properties of application
    def __init__(self, database, Validation):
        self.formColour = '#EEEAEA'

        self.fontColour = '#000000'
        self.font = 'Serif'
        self.DB = database
        self.valid = Validation
        # Calls class function 'homeScreen' which creates application home screen
        self.homeScreen()
        return

def homeScreen(self):
    #creates window using window class from ui window module
    #passes screen title and width and height of window
    win1 = UI.Window('Home',500,350,self.formColour,self.fontColour,self.font)

    #calls centrewindow method from window class to centre the window within the users screen
    win1.centreWindow()

    #takes 'header' and 'body' attributes from 'win1' object and stores them in variables 'headerFrame' and 'bodyFrame'
    headerFrame = win1.getHeader()
    bodyFrame = win1.getBody()

    win1.showTitle(160)

    #craetes title labelfor window 'win1'
    titleLabel = win1.customLabel('header','Home Page',10)
    titleLabel.grid(column=1,row=1)
    titleLabel['fg']= '#747373'

    courseLabel = win1.customLabel('body', 'To view and edit courses:',10)
    courseLabel.grid(row=0,column=1, pady=10)

    #craeyes button to navigate to screen displaying the user's courses
    courseButton= Button(bodyFrame,text="Courses", command= lambda:[win1.destroyWindow(),self.courseScreen()])
    courseButton.grid(row=1,column=1)
    courseButton['bg']=win1.getColour()
    courseButton['fg']= win1.getFontColour()
    courseButton['font']= (self.font,10)

    taskLabel = win1.customLabel('body', 'To view and edit tasks:',10)
    taskLabel.grid(row=2,column=1, pady=10)

    #creates button to navigate to user's tasks
    taskButton= Button(bodyFrame,text="Tasks", command= lambda:[win1.destroyWindow(),self.taskScreen()])
    taskButton.grid(row=3,column=1,padx=10)
    taskButton['bg']=win1.getColour()
    taskButton['fg']= win1.getFontColour()
    taskButton['font']= (self.font,10)

    settingsLabel = win1.customLabel('body', 'To view and edit settings:',10)
    settingsLabel.grid(row=4,column=1, pady=10)
    settingsButton=Button(bodyFrame,text = 'Settings', command= lambda:[win1.destroyWindow(),self.settingsScreen()])
    settingsButton.grid(row=5,column=1,)
    settingsButton['bg']=win1.getColour()
    settingsButton['fg']= win1.getFontColour()
    settingsButton['font']= (self.font,10)

    win1.mainloop()
    return

def settingsScreen(self):
    #craetes window using window class from ui window module
    #passes screen tile and width and height of window
    settingsWin = UI.Window('settings',400,300,self.formColour,self.fontColour,self.font)
    #calls centrewindow meehtod from window class to centre the window within the users screen
    Se

if __name__ == "__Main__":
    print("running main.py")

