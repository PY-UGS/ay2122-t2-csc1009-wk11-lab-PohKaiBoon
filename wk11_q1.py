class calculator: # calculator class
    input1= 0.0 
    input2= 0.0
    
    def __init__(self, h, m): #constructor 
        self.input1 = h # self is equivalent to this. in java
        self.input2 = m
    
    def adder(self): # Add method
        return self.input1+self.input2
    def subtractor(self): # Subtract method
        return self.input1-self.input2
    def multiplier(self): # Multiply method
        return self.input1*self.input2
    def divider(self): # Divide method
        return self.input1/self.input2
    def clear(self): # Clear the calculator, set it back to 0
        self.input1=0
        self.input2=0

one= float(input("Enter number #1: "))  # input first number
two= float(input("Enter number #2: "))  # input second number

c = calculator(one,two) # create new object, add the two numbers input as the parameters

print("Addition: "+str(c.adder())) 
print("Subtraction: "+str(c.subtractor()))
print("Multiplication: "+str(c.multiplier()))
print("Division: "+str(c.divider()))

# check if numbers will be cleared
print("Numbers before clear: "+ str(c.input1)+ " "+ str(c.input2))
c.clear()
print("Numbers after clear: "+ str(c.input1)+ " "+ str(c.input2))