# Class Program
class Calculator:
    def calculate(self, num1, num2, action):
        if action == 1:
            return num1 + num2
        elif action == 2:
            return num1 - num2
        elif action == 3:
            return num1 * num2
        else:
            return num1 / num2
    

cal = Calculator()
cal.calculate(2,3,1)
# OUTPUT : 5


 