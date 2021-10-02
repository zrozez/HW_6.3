class Credit:

    def __init__(self, amount_of_credit, amount_of_fees, procent):
        self.amount_of_credit = amount_of_credit
        self.amount_of_fees = amount_of_fees
        self.procent = procent

    @property
    def summ(self):
        self.credit_calc = self.amount_of_credit + self.amount_of_fees + self.procent
        return self.credit_calc

print(Credit(40000, 350, 78).summ)
    