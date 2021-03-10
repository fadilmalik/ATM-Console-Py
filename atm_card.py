class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def checkFirstPin(self):
        return self.defaultPin

    def checkFirstBalance(self):
        return self.defaultBalance
