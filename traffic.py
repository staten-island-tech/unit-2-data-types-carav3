# variables for eastbound/westbound traffic
x = True
y = False

def truthy(x,y):
    if x == y:
        print("False")
    elif not(x != y):
        print("True")
truthy(x,y)

# create a function that accepts two arguments