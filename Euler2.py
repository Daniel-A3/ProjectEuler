# Finds the sum of even valued terms in a fibonacci sequence under 4 Million.
end = 4000000
sum = 0
next = 2
current = 1
while next < 4000000:
    if next % 2 == 0:
        sum += next
    temp = next
    next = next + current
    current = temp

print(sum)