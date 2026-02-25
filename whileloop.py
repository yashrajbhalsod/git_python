#print number from 1 to 5 using while loop
"""i = 1
while i <= 5:
    print(i)
    i += 1

#sum of numbers take user input using while loop
    n = int(input("Enter how many numbers you want to add: "))

    count = 1
    total = 0

    while count <= n:
        num = int(input("Enter number: "))
        total += num
        count += 1

    print("Sum =", total)
#print odd number between 1 to 20 using while loop
    i = 1
    while i <= 20:
        if i % 2 != 0:
            print(i)
i += 1
#print table of 4 using while loop
i = 1
while i <= 10:
    print("4 x", i, "=", 4 * i)
    i += 1
#print reversse number using while loop
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse number =", reverse)
#print largest number using while loop
numbers = [10, 45, 23, 89, 12]

i = 0
largest = numbers[0]

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("Largest number =", largest)"""
#print even number bitween 1 to 20 using while loop
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1