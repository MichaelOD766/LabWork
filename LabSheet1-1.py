# LabSheet1: Question 1 - Area of Triangle
# x = s, y = s1, z = s2
x = input("x:")
y = input("y:")
z = input("z:")

area = (float(x) *(float(x) - float(y)) * (float(x) - float(z)) * (float(x) - float(z))) ** 0.5

print(area)