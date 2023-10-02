# challenge 4

factors = set()
m = input("input a number: ")
n = int(m)

a = int()

for a in range(1, n + 1):
    if n % a == 0:  # remainder is zero
        factors.add(a)
print("Factors of {} are {}".format(n, factors))

quit()