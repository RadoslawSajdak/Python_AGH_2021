## Radosław Sajdak

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

result = 0

for x, y in zip(a, b):
    result += x*y
print( result )