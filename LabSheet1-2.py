# LabSheet1: Question 2 - Factorial => Also LabSheet 2: Question

# Number we want the factorial of it stored as 'Num'
Num = input("Number: ")

# Set the 'Factorial' variable as random number
Factorial = 1

# Use an if statement to check if the number is neg    
if int(Num) < 0:
    print("Factorial does not exist for negative numbers")

# Set an else if statment for 0
elif int(Num) == 0:
    print("The factorial of 0 is 1")

# For loop and range function is used if the number is positive to calculate the factorial 
else:
    for i in range(1, int(Num) + 1):
        Factorial = Factorial * i

# Result is printed with message
    print("The factorial of",int(Num),"is",Factorial)


