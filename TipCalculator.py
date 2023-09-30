b = input("How much is the bill?")
t = input("How much is the tip, in dollars?")
# a will represent the total amount paid

bill = float(b)
percent = int(t)

total = bill + percent
print(f"The total amount is {total}")
print(f"If the bill is {bill} and the tip is {percent} then your total is {total}")

p = input("Do you want to try this a different way? Type y or n.")

if p == ("y"):
    print("We will continue.")

elif p == ("n"):
    print("Ok, maybe next time.")
    quit()

else:
    print("Error, incorrect response. Program has terminated.")
    quit()


b = input("How much is the bill with the tax included?")
print("You're calculating the tip after tax.")
p = input("How much percent tip would you like to leave?")

# a will represent the total amount paid

bill = float(b)
percent = float(p)

pdecimal = percent / 100
tip = bill * pdecimal

total = bill + tip

print(f"Your tip amount is {tip}")
print(f"The total amount is {total}")

quit()