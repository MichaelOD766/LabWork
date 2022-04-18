# LabSheet2: Question 2 - Prime Number

# Input your number to check
x = int(input("Positive Number: "))

# Function to determine if the number is prime or not
def prime(num):
    """ Check if the number is greater than 1 (if it isnt then it will return 
        false), if it is then it will checkif the remainder after dividing it 
        by the numbers between 1 and itself is zero. If it is zero then the output
        will be false. Otherwise it will be true
    """
    if num > 1:
        for n in range(2, int(num)):
            if num % n == 0:
                return False
        return True
    else:
        return False
# Executes the function with the supplied number
print(prime (x))