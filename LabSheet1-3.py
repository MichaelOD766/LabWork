# LabSheet1: Question 3 - Quadratic Function

import math as math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def findRoots(a, b, c):
    dis_form = b*b - 4*a*b*c
    sqrtVal = math.sqrt(abs(dis_form))

    if dis_form > 0:
        print("Real and Different roots")
        print((-b + sqrtVal) / (2 * a))
        print((-b - sqrtVal) / (2 * a))
    
    elif dis_form == 0:
        print("Real and Same roots")
        print(-b / (2 * a))
        
    else:
        print("Complex Roots")
        print(-b / (2 * a), " + i", sqrtVal)
        print(-b / (2 * a), " - i", sqrtVal)


if a == 0:
    print("Input correct quadratic equation")

else:
    findRoots(a, b, c)
