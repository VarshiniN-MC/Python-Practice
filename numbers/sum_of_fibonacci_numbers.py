#Sum of Fibonacci numbers
n = int(input("Enter number of terms: "))
a = 0
b = 1
sum = 0
print("Fibonacci series: ")
for i in range(n):
    print(a, end=" ")
    sum = sum + a
    c = a + b
    a = b
    b = c
print("\nSum of Fibonacci numbers =", sum)
