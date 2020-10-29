#Homework 8.2
#Oct. 28, 2020

from random import randrange

x = 10
print("INTEGER DIVISION PRACTICE")

while x > 0:
    a = randrange(5)
    b = randrange(12)
    if a == 0:
        continue
    elif (b%a) != 0:
        continue
        
    try:
        q = str(b)+"/"+str(a)+"=    "
        ans = int(input(q))
    except ValueError:
        print("Please enter integers only!!!")
        continue
    if (b/a) == ans:
        print("CORRECT")
        x = x - 1
    else:
        print("INCORRECT")
        x = x - 1