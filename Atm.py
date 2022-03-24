class Atm (object):
    def __init__(self,company,color,perTransactionLimit):
        self.company=company
        self.color=color
        self.perTransactionLimit=perTransactionLimit

    def CashWithdrawl (self):
        print('WithDrawing the cash')

    def BalanceEnquiry (self):
        print('BalanceEnquiry')

    def SavingAcount(self):
        print('Opening saving Account') 



IciciBank=Atm('Icici Bank','REd,orange and white',15000)
IciciBank.CashWithdrawl()


