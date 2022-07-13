# Write a program which accepts a real number and shows the sum of its digits.

stNum = input('Please enter a real number: ')
sum = 0
for el in stNum:
    if el.isdigit():
        sum += int(el)
print(f"Summa of digits is: {sum}")