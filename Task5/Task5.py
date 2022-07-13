# Implement a list shuffling algorithm.
import random

testArray = [random.randint(-10, 10) for _ in range(10)]
print(f'Before shuffle: {testArray}')

for _ in range(10):
    pos1 = random.randint(0, 9)
    pos2 = random.randint(0, 9)
    testArray[pos1], testArray[pos2] = testArray[pos2], testArray[pos1]

print(f'Shuffled array is: {testArray}')