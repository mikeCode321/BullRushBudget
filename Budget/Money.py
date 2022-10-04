class Money:

    def __init__(self):
        self.amount = 0
        self.isOverBudget = False

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getIsOverBudget(self):
        return self.isOverBudget

    def setIsOverBudget(self, cond):
        self.isOverBudget = cond


