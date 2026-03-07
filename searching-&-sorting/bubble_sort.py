#Bubble sort  
numbers = [50, 39, 15, 40, 5]
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("numbers after sorting:", numbers)
