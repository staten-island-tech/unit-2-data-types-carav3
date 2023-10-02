# challenge 3: function accepting bill value and tip

bill = float (input("Please enter your bill value."))
tip = float()

service_choice = input("Was the service bad, okay, good, or great?")
if service_choice == "bad":
    print("0% tip should be given.")
    tip = 0
    print("The tip amount in dollars is $", tip)
elif service_choice == "okay":
    print("15% tip should be given.")
    tip = bill * 0.15
    print("The tip amount in dollars is $", tip)
elif service_choice == "good":
    print("20% tip should be given.")
    tip = bill * 0.20
    print("The tip amount in dollars is $", tip)
elif service_choice == "great":
    print("25% tip should be given.")
    tip = bill * 0.25
    print("The tip amount in dollars is $", tip)
else:
    print("Unable to give a tip calculation. Try again.")