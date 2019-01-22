class Calculator():
    """ Module for HW 1: a simple calculator.

    Attributes:

    num: a single number input into a calculator object when it's initialized,
    set to zero if none given
    
    """
    
    def __init__(self, num=0):
        self.num = num
        
    def add(self, val):
        self.num = self.num + val
        return self
    
    def sub(self, val):
        self.num = self.num - val
        return self
    
    def div(self, val):
        self.num = self.num / val
        if val == 0:
            raise DivideByZero("What in god's name are you doing?")
        return self
    
    def mul(self, val):
        self.num = val * self.num
        return self
    
    def clr(self):
        self.num = 0
        
    def result(self):
        return self.num
