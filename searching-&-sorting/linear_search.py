#Linear Search
numbers = [50, 39, 15, 40, 5]
key = int(input("Enter the element to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")
