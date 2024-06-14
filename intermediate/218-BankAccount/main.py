class BankAccout:

    def __init__(self, bankName: str, ownerName: str, savings: int) -> None:

        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings

    def withdrawMoney(self, withdrawAmount: int) -> int:

        withdrawal_limit = int(self.savings * 0.2)

        if withdrawAmount >= withdrawal_limit:
            self.savings = int(self.savings - withdrawal_limit)
        else:
            self.savings = int(self.savings - withdrawAmount)

        return self.savings

    def depositMoney(self, depositAmount: int) -> int:

        commission = 100

        if self.isThereACommision():
            self.savings = self.savings + depositAmount - commission
        else:
            self.savings = self.savings + depositAmount

        return self.savings

    def isThereACommision(self) -> bool:
        if self.savings <= 20000:
            return True
        return False

    def pastime(self, days: int) -> float:

        daily_deposit_amount = 0.25

        return self.savings + days * daily_deposit_amount


user1 = BankAccout("Chase", "Claire Simmmons", 30000)
user2 = BankAccout("Bank of America", "Remy Clay", 10000)

print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))
