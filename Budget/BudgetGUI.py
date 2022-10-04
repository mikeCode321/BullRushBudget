from tkinter import *
from tkinter import ttk
from datetime import date

from ParseReport import ParseReport

mainWindow = Tk()
mainWindow.title("Bull Rush Budgeting")
mainWindow.geometry('675x550')
currentDate = date.today().strftime("%B %d, %Y")


# main at bottom of file
# constructor calls on set up of gui
# button bindings will be in the setup gui as well
class BudgetGUI:

    def __init__(self, master):
        self.currentBudgetPositionY = 200

        self.currentDateLabel = Label(master, text=currentDate)
        self.currentDateLabel.pack()

        self.terminateSessionButton = Button(master, text="Terminate Session", command=master.destroy)
        self.terminateSessionButton.place(x=500, y=500)

        self.reportPathLabel = Label(master, text="File Path")
        self.reportPathLabel.place(x=375, y=75)

        self.ReportEntry = Entry(master, width=15)
        self.ReportEntry.place(x=435, y=75)

        self.ReportGenerate = Button(master, text="Submit", command=self.updateTreeView)
        self.ReportGenerate.place(x=585, y=75)

        self.budgetTitle = Label(master, text="Budget", font=("Times New Roman", 20))
        self.budgetTitle.place(x=500, y=120)

        self.budgetCategoryEntry = Entry(master, width=15)
        self.budgetCategoryEntry.insert(0, "Add New Category...")
        self.budgetCategoryEntry.place(x=430, y=150)
        self.budgetCategoryEntry.bind("<FocusIn>", self.temp_text)

        self.budgetAddCategory = Button(master, text="Add", command=self.addCategory)
        self.budgetAddCategory.place(x=580, y=150)

        self.frame = Frame(master)
        self.frame.pack(side="left")

        self.tree = ttk.Treeview(self.frame, height=20)
        self.tree.pack()

        # scrollbar = ttk.Scrollbar(master, orient=VERTICAL, command=tree.yview)
        # tree.configure(yscrollcommand=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky='ns')

        # self.scroll_bar = Scrollbar(self.frame, orient="vertical")
        # self.scroll_bar.config(command=self.reportListBox.yview)
        # self.scroll_bar.pack(side="left", fill="y")
        #
        # self.reportListBox.config(yscrollcommand=self.scroll_bar.set)

    def updateTreeView(self):
        csvFileParsed = ParseReport(self.callReportToGenerate())
        column = tuple(csvFileParsed.getHeadings())
        self.tree.destroy()
        self.tree = ttk.Treeview(self.frame, columns=column,show='headings', height=20)
        self.tree.heading(column[0], text='Description')
        self.tree.column(column[0], minwidth=70, width=125, stretch=NO)
        self.tree.heading(column[1], text='Earnings/Expenses')
        self.tree.column(column[1], minwidth=80, width=105, stretch=NO)
        self.tree.heading(column[2], text='Total')
        self.tree.column(column[2], minwidth=50, width=55, stretch=NO)
        self.tree.pack()

        listOfRows = csvFileParsed.generateRows()
        print(listOfRows)
        for i in listOfRows:
            self.tree.insert('', END, values=i)

    def temp_text(self, *args):
        self.budgetCategoryEntry.delete(0, "end")

    def addCategory(self):
        self.currentBudgetPositionY += 30
        texts = self.budgetCategoryEntry.get()
        budgetCategoryLabel = Label(mainWindow, text=texts)
        budgetCategoryLabel.place(x=350, y=self.currentBudgetPositionY)

    def callReportToGenerate(self):
        reportPath = self.ReportEntry.get()
        return reportPath


budgetGui = BudgetGUI(mainWindow)
mainWindow.mainloop()
