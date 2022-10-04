import csv

# drop csv file parse it then store data in a data structure for description e/e and total
# take variables display to screen user selects budget category
# class needs to compute budget totals in gui

class ParseReport:

    def __init__(self, reportPath):
        file = open(reportPath, mode='r', encoding='utf-8-sig')
        self.csvFile = csv.DictReader(file)
        self.descriptionOfReport = [] # list of description values i.e "gas"
        self.eeOfReport = []
        self.listOfRows = []
        self.listOfHeadings = []
#get list of tuples to iterate over in gui to insert in treeview

    def generateRows(self):
        listOfDescriptions = self.getDescription()
        listOfEE = self.getEarnAndExp()
        for i in range(4):
            changeToTuple = tuple([listOfDescriptions[i], 8, 0])
            print(changeToTuple)
            self.listOfRows.append(changeToTuple)
        return self.listOfRows

    def getDescription(self):
        for rows in self.csvFile:
            self.descriptionOfReport.append(rows['description'])
        return self.descriptionOfReport

    def getEarnAndExp(self):
        for rows in self.csvFile:
            self.eeOfReport.append(rows[0])
        return self.eeOfReport

    def ssss(self):
        for value in self.csvFile:
            print(value)

    def getHeadings(self):
        return self.csvFile.fieldnames

    def computeEarningsAndExpenses(self, listOfCheckedEE):
        total = 0
        for value in listOfCheckedEE:
            total += int(value)
        return total


# g = ParseReport("/Users/maiklzaki/Desktop/EarnExpReport.csv")
#
# print(g.getDescription())
# print("h")
# print(g.getEarnAndExp())