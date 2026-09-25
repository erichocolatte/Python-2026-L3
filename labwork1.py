# Ex1
from numpy import pi
r = float(input("Enter circle radius? "))
area = pi*(r**2)
print("Circle area = ", round(area, 0))

# Ex2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius*1.8) + 32
print(f"{celsius} (C) = {fahrenheit} (F)")

# Ex3
from math import sqrt
n = int(input("Enter a number? "))
if n < 2:
  print(f"{n} is not a prime number")
else:
  prime = True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      prime = False
      break
  if prime:
      print(f"{n} is a prime number")
  else:
      print(f"{n} is NOT a prime number")

# Ex 4
from math import sqrt
n = int(input("Enter a number? "))
sum = 1
for i in range(2, int(sqrt(n)) + 1):
  if n % i == 0:
    sum += i
    if i != n//i:
      sum += (n//i)
if n>1 and sum == n:
  print(f"{n} is a perfect number")
else:
  print(f"{n} is NOT a perfect number")

# Ex5
color_list = ['white', 'black', 'red', 'blue', 'purple']
color = input("What is your favorite color? ")
position = color_list.index(color) + 1
if color in color_list:
  print(f"Your color is at index {position} in my list")
else:
  print("Sorry, I could not find your color")


# Ex6
range1 = range(7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)
print(*range1, sep = ', ')
print(*range2, sep = ', ')
print(*range3, sep = ', ')
print(*range4, sep = ', ')


# Ex7
s = input("Enter a string? ")
def remove_dollar_sign(s):
    return s.replace("$", "")
print(remove_dollar_sign(s))

# Ex8
l = [1, 4, 5, -1, 10]
def extract_even(l):
    return [x for x in l
            if x % 2 == 0]
print(extract_even(l))

# Ex9
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
  print("Please enter a positive number")
elif n == 0:
  print("0! = 1")
else:
  for i in range(n, 0, -1):
    factorial *= i
  print(f"{n}! = {factorial}")


# Ex10
n = int(input("Enter a number: "))
def get_divisors(n):
    if n == 0:
      print("Error")
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
print(get_divisors(n))



# Ex11
import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
p1 = x1, y1
p2 = x2, y2
def distance(p1, p2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(round(distance(p1,p2),2))

# Ex12
def pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() # move to next line
print(pattern(4, 5))