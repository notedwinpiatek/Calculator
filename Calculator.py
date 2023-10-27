print("Input 2 numbers")
number = False
while number != True:
    try:
        a = int(input("Number 1 = "))
        b = int(input("Number 2 = "))
        number = True
        print("Summary")
        print(a + b)
        print("Subtract")
        print(a - b)
        print("Multiplication")
        print(a * b)
        print("Division")
        if b == 0: print("It's imposible to devide by 0") 
        else: print(a / b)
    except ValueError:
        print("Invalid input. Try again.")