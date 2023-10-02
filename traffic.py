# variables for eastbound/westbound traffic
x = True
y = False

def truthy(x,y):
    if x == y:
        print("False")
    elif not(x != y):
        print("True")
truthy(x,y)

x = 48448484
y = False
print(x)
def truthy(x,y):
    if type(x) != bool or type(y)  != bool:
        print("Glitch!")
    else:
        if x == y:
            print("False")
        elif x != y:
            print("True")
        truthy(x,y)
        
# != means NOT EQUAL
# x = 48348343 would be considered a glitch
# to make sure program stays correct:

#  create a function that accepts two arguments