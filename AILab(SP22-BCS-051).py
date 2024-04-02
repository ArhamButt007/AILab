# Arham Atique
# SP22-BCS-051
# Section C

# Activity 1

print("*** Calculating Grade ***\n")    
marks = float(input("Enter your marks (1-100): "))

if(marks>=1 and marks <=100):
    if(marks<50):
        print("Your Grade is F")
    elif(marks>=50 and marks<=60):
        print("Your Grade is E")
    elif(marks>60 and marks<=70):
        print("Your Grade is D")
    elif(marks>70 and marks<=80):
        print("Your Grade is C")
    elif(marks>80 and marks<=90):
        print("Your Grade is B")
    elif(marks>90 and marks<=100):
        print("Your Grade is A")
else:
    print("Enter marks in range of 1-100")


# Activity 2

print("\nCalculating Factorial\n")    
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


number = int(input("Enter an integer number to calculate factorial: "))

fact = factorial(number)
print(f"\nFactorial of {number} is {fact}")


# Assignment

def fibonacci(num):
    x, y = 0, 1
    count = 0
    while count < num:
        print(x, end=" ")
        x, y = y, x + y
        count += 1


print("\n*** For Fabonacci Series ***\n")
num = int(input("Enter a number: "))

fibonacci(num)


