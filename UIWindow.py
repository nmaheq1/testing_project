from tkinter import *

class Window():
    def __init__(self, givenTitle, givenWidth, givenHeight, FormColour,
                 FontColour, Font):
        self.form = Tk()

        self.form.title(givenTitle)
        self.form['bg'] = FormColour
        self.form.resizable(False, False)
        self.width = givenWidth
        self.height = givenHeight
        self.header = Frame(self.form)
        self.header.grid(row=0, column=1, pady=10)
        self.header['bg'] = FormColour
        self.body = Frame(self.form)
        self.body.grid(row=1, column=1)
        self.body['bg'] = FormColour
        self.formColour = FormColour
        self.fontColour = FontColour
        self.font = Font
        self.title = 'Student Track'

    def mainloop(self):
        self.form.mainloop()
        return

    def showTitle(self, Padx):
        label = self.customLabel('header', self.title, 20)

        label.grid(row=0, column=1, padx=Padx)
        return

    def getTitle(self):
        return self.title

    def getFont(self):
        return self.font

    def setFont(self, newFont):
        self.font = newFont

        return

    def getColour(self):
        return self.formColour

    def setColour(self, colour):
        self.formColour = colour

        return

    def getFontColour(self):
        return self.fontColour

    def setFontColour(self, fontColour):
        self.fontColour = fontColour

        return self.fontColour

    def getScreen(self):
        return self.form

    def getHeader(self):
        return self.header

    def getBody(self):
        return self.body

    def centreWindow(self):

    # Get screen width and height
        screenWidth = self.form.winfo_screenwidth()
        screenHeight = self.form.winfo_screenheight()
        # Calculate position of x and y coordinates
        x = (screenWidth / 2) - (self.width / 2)
        y = (screenHeight / 2) - (self.height / 2)
        # Sets the position of the window
        self.form.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        return

    # Creates custom labels that fit the UI theme and customisation
    def customLabel(self, frame, txt, fntSz):
        if frame == 'body':
            frame = self.body

        elif frame == 'header':
            frame = self.header
        label = Label(frame, text=txt)
        label['bg'] = self.getColour()
        label['fg'] = self.getFontColour()
        label['font'] = (self.font, fntSz)
        return label

    def destroyWindow(self):
        self.form.destroy()
        return
