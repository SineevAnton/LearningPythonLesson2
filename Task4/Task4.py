# Create a list of N elements, filled with numbers from [-N, N].
# Find the prod of elements in defined positions.
import random

num = int(input('Please, enter a number: '))
positionCount = random.randint(1, num) # value to chose how many numbers from initial array we will multiply
numbers = []
positionsForMultiply = []

for _ in range(num):
    numbers.append(random.randint(-num, num))

for _ in range(positionCount):
    positionsForMultiply.append(random.randint(0, num-1))

print(f'Initial list is: {numbers}')
print(f'List of indexes is: {positionsForMultiply}')

prod = 1
for i in positionsForMultiply:
    prod *= numbers[i]

print(f'Prod of numbers on defined positions is: {prod}')