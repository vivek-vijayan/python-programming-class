# Calculator program

def calculator(number1, number2, action):
    if action == 1:
        return number1 + number2
    elif action == 2:
        return number1 - number2
    elif action == 3:
        return number1 * number2
    else:
        return number1 / number2

a,b = input("Enter the numbers : ").split(' ')
action = int(input("Select your action: \n 1. Addition \n 2. Subtraction \n 3. Multiply \n 4. Division \n"))

if(action < 5 and action > 0 ):
    print(calculator(int(a), int(b),action))
else:
    print("Error : Invalid option")
