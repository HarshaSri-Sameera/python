# calculator.py
to do some arithemetic operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('Give any following operations for two numbers')
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divide")

while True:
    user = input("enter ur choice")
    if user in ('1', '2', '3', '4'):
        num1 = float(input("enter first number"))
        num2 = float(input("enter second number"))

        if user == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif user == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif user == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif user == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        break
    else:
        print('Invalid choice')
