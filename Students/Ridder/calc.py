class Calculator():
    """ Module for HW 1: a simple calculator.

    Attributes:

    num: a single number input into a calculator object when it's initialized,
    set to zero if none given
    
    """
    
    def __init__(self, num=0):
        self.num = num
        
    def add(self, val):
        #Adds value to num.
        self.num = self.num + val
        return self
    
    def sub(self, val):
        #Subtracts value from num.
        self.num = self.num - val
        return self
    
    def div(self, val):
        #Divides num by val.
        self.num = self.num / val
        if val == 0:
            raise DivideByZero("What in god's name are you doing?")
        return self
    
    def mul(self, val):
        #Multiplies num by val.
        self.num = val * self.num
        return self
    
    def clr(self):
        #Clears num by setting it to zero.
        self.num = 0
        
    def result(self):
        #Assigning a proper name to num.
        return self.num
