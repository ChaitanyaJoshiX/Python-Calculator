"""
Ask user for mathematical expression.
Ask to separate with space (necessary for seperating operators and values).
Author : @ChaitanyaJoshiX
"""
import math
def Add():
    if i == 0:
        added = values[i] + values[i+1]
        return added
    else:
        added = answer + values[i+1]
        return added

def Subtract():
    if i == 0:
        added = values[i] - values[i+1]
        return added
    else:
        added = answer - values[i+1]
        return added

def Multiply():
    if i == 0:
        added = values[i] * values[i+1]
        return added
    else:
        added = answer * values[i+1]
        return added

def Divide():
    if i == 0:
        added = values[i] / values[i+1]
        return added
    else:
        added = answer / values[i+1]
        return added

def Power():
    if i == 0:
        added = values[i] ** values[i+1]
        return added
    else:
        added = answer ** values[i+1]
        return added


print("Welcome to the Calculator!")
print("~"*27)
print("This calculator supports the following functions : ")
print("•Addition (+)\n•Subtraction (-)\n•Multiplication (*)")
print("•Division (/)\n•Power (^)")
print("~"*36)
print("IMPORTANT : Please separate your equation with spaces.")
print("Example : 1 + 2 * 4 instead of 1+2*4")
print("~"*36)
eqn = input("Enter your mathematical expression : ")
eqnList = eqn.split(' ')
values = []
operators = []

for temp in eqnList:
    try:
        float(temp)
        values.append(float(temp))
    except:
        operators.append(str(temp))
for i in operators:
    if i == '':
        operators.remove('')

answer = 0
i = 0
for oper in operators:
    if oper == '+':
        answer = Add()
        i += 1
    elif oper == '-':
        answer = Subtract()
        i += 1
    elif oper == '*':
        answer = Multiply()
        i += 1
    elif oper == '/':
        answer = Divide()
        i += 1
    elif oper == '^':
        answer = Power()
        i += 1
    else:
        print("Invalid operator.")

print("~"*27)

if answer.is_integer() == True:
    print("Answer =",answer)
    print("~"*15)
else:
    roundchoice = input("Would you like to round off your answer? (y/n) : ")
    if roundchoice == 'y':
        print("~"*15)
        print("Table\n1 : Whole Number\n2 : 2 Decimal places")
        print("~"*15)
        digit = int(input("How many digits would you like to round off to? (1/2) : "))
        if digit == 1:
            rounded = round(answer)
            print("Answer =",rounded)
            print("~"*15)
        elif digit == 2:
            print("Answer =",int(math.ceil(answer*100)/100))
            print("~"*15)
    else:
        print("Answer =",answer)
        print("~"*15)

"""
Author : @ChaitanyaJoshiX
"""
