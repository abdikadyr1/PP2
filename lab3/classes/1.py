class strgp:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())
        
p1 = strgp()
p1.getString()
p1.printString()