# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Create an array of n numbers of sequence (1+1/n)^n and print the sum of array elements

n = int(input('Please enter a number: '))
resultArr = []
for i in range(1, n+1):
    resultArr.append((1 + 1/i)**i)

print("Summa is: {:.2f}".format(sum(resultArr)))