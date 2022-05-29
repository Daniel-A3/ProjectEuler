# Finds the sum of all multiples of 3 or 5 under 1000
sum = 0

for i in range(0, 1000):
    if i % 5 == 0:
        sum += i
    elif i % 3 == 0:
        sum += i

print(sum)