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



