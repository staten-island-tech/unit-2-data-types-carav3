x = int(input("enter a number to be factored."))
factors = []
for i in range(1, x+1):
    if x % i == 0:
        factors.append(i)
print(factors)

y = int(input("enter a number to be factored."))
gcf = []
for i in range(1, y+1):
    if y % i == 0 and x % i == 0:
        gcf.append(i)
print(gcf)

if len(factors) > len(gcf):
    z = len(factors)
else:
    z = len(gcf)

g = 5
for i in range(z):
    if factors[i] in gcf:
        g = factors[i]

print(f"The greatest common factor of your two numbers is {g}")


quit()