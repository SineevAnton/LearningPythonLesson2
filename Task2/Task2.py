# Write a program which accepts a number returns all prods of digits from 1 to number.

num = int(input('Please enter a number: '))
prods = [1]
for i in range(2, num + 1):
    prods.append(prods[i-2] * i)
print(prods)