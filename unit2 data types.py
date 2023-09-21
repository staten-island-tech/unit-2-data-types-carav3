#string/string values

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z) 

#a = len(input)
#make a code for counting the letters in the input sentence
#I'm not sure how to do this part.
#print("The number of letters in your sentence are:"{a})


#booleans and control flow

day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
