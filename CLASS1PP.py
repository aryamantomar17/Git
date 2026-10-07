x = 17
y = 58 
sum = x + y 
print("the sum of", x, "and", y, "is", sum)

"""new program"""

x = "Student marks"
z = 79 
marks = 67
print(marks==z)
print(x, "are the marks of the student but they are not equal to", z)

"""new program"""

length = 7
breadth = 18
area = length * breadth
print("the area of the rectangle would be", area)


"""new program"""

price = 100
quantity = 5
total_cost = price * quantity
print("the total cost of the items would be", total_cost)

"""new program"""

price = 78
quantity = 3
total_cost = price * quantity
if total_cost > 200:
    print("the total cost of the items is greater than 200")
else:    
    print("the total cost of the items is less than or equal to 200")

    print("the total cost of the items would be", total_cost)

    """new program"""

temperature = 27
if temperature > 30:
    print("it is a hot day outside")
elif temperature < 20:
    print("it is a cold day outside")
else:
    print("it is a pleasant day outside")

    """new program"""
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 > n2 and n1 > n3:
    print(n1, "is the largest number")
elif n2 > n1 and n2 > n3:
    print(n2, "is the largest number")  
else:
    print(n3, "is the largest number")  