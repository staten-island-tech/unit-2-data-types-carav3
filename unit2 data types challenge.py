#challenge #1 code below
#CHALLENGES HERE NOT COUNTING MAD LIBS PROJECT OR TIP CALCULATOR WHICH ARE SEPARATE


x = input("Type in a sentence.")
print("Your sentence is ", x)
y = x.split( )
print(y)

z = len(y)
print(z)



#challenge 2 - learning "modulo" 
#notes below...
# "%" and "//" are different
# % = remainder
# // = number of whole numbers in the answer
#USE INT TO CONVERT IT

a = input

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

# challenge 3: function accepting bill value and tip

z = input("Please say your bill value.")
print(z)
service_choice = input("Was the service bad, okay, good, or great?")
if service_choice == "bad":
    print("0% tip should be given.")
elif service_choice == "okay":
    print("15% tip should be given.")
elif service_choice == "good":
    print("20% tip should be given.")
elif service_choice == "great":
    print("25% tip should be given.")
else:
    print("Unable to give a tip calculation. Try again.")


# challenge 4
#REVIEW THIS***
factors = set()
m = input("Give me a number.")
n = int(m)

for a in range(1, n + 1):
    if n % a == 0:  # remainder is zero
        factors.add(a)
print("Factors of {} are {}".format(n, factors))


#challenge 5 (below)

#get a list of factors for one number and the other number
#compare the two lists, take each individual list and match up the factors
#for loop to go through one list of numbers
#check if the number is in the other list.  by writing "in"
#if x in...

#add numbers to a list???

factors = set()
y = input("Give me your first number.")
t = int(y)

for a in range(1, t +1):
    if t % a == 0: 
        factors.add(a)
print("Factors (1st number) of {} are {}".format(t, factors))

factors = set()
p = input("Give me your second number.")
u = int(p)

for b in range(1, u +1):
    if u % b == 0:
        factors.add(b)
print("Factors (2nd number) of {} are {}".format(u, factors))


li1 = t.split()
li2 = u.split()

print(li1)