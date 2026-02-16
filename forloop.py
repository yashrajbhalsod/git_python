# prints numbers from 1 to 5
for i in range(1,6):
    print(i)
# print a message 3 times
    for i in range(3):
        print("hello")
#print numbers from 1 to 10
    for i in range(1,11):
        print(i)
#print even numbers from 1 to 20 
    for i in range(1,21):
        if i%2==0:
            print(i)
#print odd numbers from 1 to 15            
    for i in range(1,15):
        if i%2!=0:
            print(i)
#print table of 5
    for i in range(1,11):
        print("5 x",i,"=",5*i)
#print characters of a string
    name="atmiya"
    for letter in name:
        print(letter)
#sum of nubers from 1 to 10
    total=0
    for i in range(1,11):
        totle=totle+i
    print("sum is",total)
#print list elements
    numbers=[1,2,3,4,5]
    for num in numbers:
        print(num)