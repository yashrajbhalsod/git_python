Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x="Welcome"
... >>> print(x)
... Welcome
... >>> x="Rajesh Kumar /n Flat No. 101,Sunshine Apartments /n MG Road,Sector 15 /n Rajkot,/nPincode:360004/n India."
... >>> print(x)
... Rajesh Kumar /n Flat No. 101,Sunshine Apartments /n MG Road,Sector 15 /n Rajkot,/nPincode:360004/n India.
... >>> x="Rajesh Kumar \n Flat No. 101,Sunshine Apartments \n MG Road,Sector 15 \n Rajkot,\nPincode:360004\n India."
... >>> print(x)
... Rajesh Kumar 
...  Flat No. 101,Sunshine Apartments 
...  MG Road,Sector 15 
...  Rajkot,
... Pincode:360004
...  India.
... >>> x=150
... >>> y=120.50
... >>> print(x+y)
... 270.5
... >>> print(x-y)
... 29.5
... >>> print(x*y)
... 18075.0
... >>> print(x/y)
... 1.2448132780082988
SyntaxError: invalid syntax
r = float(input("Enter radius: "))

area = 3.14 * r * r
circumference = 2 * 3.14 * r

print("Area of Circle =", area)
print("Circumference of Circle =", circumference)
SyntaxError: multiple statements found while compiling a single statement
print("Circumference of Circle =", circumference)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("Circumference of Circle =", circumference)
NameError: name 'circumference' is not defined

r = float(input("Enter radius: "))

area = 3.14 * r * r
circumference = 2 * 3.14 * r

print("Area of Circle =", area)
print("Circumference of Circle =", circumference)
SyntaxError: multiple statements found while compiling a single statement
print("Circumference of Circle =", circumference)
SyntaxError: multiple statements found while compiling a single statement
r = float(input("Enter radius: "))

Enter radius: 3
area = 3.14 * r * r
circumference = 2 * 3.14 * r
print("Area of Circle =", area)
Area of Circle = 28.259999999999998
print("Circumference of Circle =", circumference)
Circumference of Circle = 18.84
p = float(input("Enter Principal: "))
Enter Principal: 8
r = float(input("Enter Rate of Interest: "))
Enter Rate of Interest: 599
t = float(input("Enter Time (years): "))
Enter Time (years): 2
si = (p * r * t) / 100

print("Simple Interest =", si)
SyntaxError: multiple statements found while compiling a single statement
print("Simple Interest =", si)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("Simple Interest =", si)
NameError: name 'si' is not defined
si = (p * r * t) / 100

print("Simple Interest =", si)
SyntaxError: multiple statements found while compiling a single statement

print("Simple Interest =", si)
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    print("Simple Interest =", si)
NameError: name 'si' is not defined
a = (p * r * t) / 100

print("Simple Interest =", a)
SyntaxError: multiple statements found while compiling a single statement
print("Simple Interest =", a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print("Simple Interest =", a)
NameError: name 'a' is not defined
p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100

print("Simple Interest =", si)

SyntaxError: multiple statements found while compiling a single statement
p = float(input("Enter Principal: "))
Enter Principal: ya
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    p = float(input("Enter Principal: "))
ValueError: could not convert string to float: 'ya'
p = float(input("Enter Principal: "))
Enter Principal: 5
r = float(input("Enter Rate of Interest: "))
Enter Rate of Interest: 599
t = float(input("Enter Time (years): "))

Enter Time (years): 5
si = (p * r * t) / 100

print("Simple Interest =", si)
Simple Interest = 149.75
length = float(input("Enter length: "))

Enter length: 5
width = float(input("Enter width: "))

Enter width: 5
perimeter = 2 * (length + width)

print("Perimeter of Rectangle =", perimeter)

Perimeter of Rectangle = 20.0
length = float(input("Enter length: "))
Enter length: 45
width = float(input("Enter width: "))

Enter width: 5
area = length * width
perimeter = 2 * (length + width)
SyntaxError: multiple statements found while compiling a single statement
area = length * width
perimeter = 2 * (length + width)
print("Area of Rectangle =", area)

Area of Rectangle = 225.0
print("Perimeter of Rectangle =", perimeter)

Perimeter of Rectangle = 100.0
a = float(input("Enter side a: "))

Enter side a: 5
>>> b = float(input("Enter side b: "))
... 
Enter side b: 6
>>> c = float(input("Enter side c: "))
... 
Enter side c: 4
>>> perimeter = a + b + c
... 
>>> print("Perimeter of Triangle =", perimeter)
... 
Perimeter of Triangle = 15.0
>>> side = float(input("Enter side: "))
Enter side: 56
>>> area = side * side
... 
>>> perimeter = 4 * side
... 
>>> print("Area of Square =", area)
Area of Square = 3136.0
>>> print("Perimeter of Square =", perimeter)
... 
Perimeter of Square = 224.0
>>> side = float(input("Enter side: "))
... 
Enter side: 25
>>> perimeter = 4 * side
... 
>>> print("Perimeter of Square =", perimeter)
... 
Perimeter of Square = 100.0
