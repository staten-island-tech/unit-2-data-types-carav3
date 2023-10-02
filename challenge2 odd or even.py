#challenge 2 - learning "modulo" 
#notes below...
# "%" and "//" are different
# % = remainder
# // = number of whole numbers in the answer
#USE INT TO CONVERT IT

a = input("Give me a number, and I'll say if it's odd or even.")

x = int(a)
print(type(x))

y = x % 2


if y == 0:
    print("Your number is even.")

elif y > 0:
    print("Your number is odd.")

else:
    print("Your number is odd.")