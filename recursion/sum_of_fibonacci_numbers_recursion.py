#Sum of Fibonacci numbers using recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter number of terms: "))
sum = 0
print("Fibonacci series:")
for i in range(n):
    val = fib(i)
    print(val, end=" ")
    sum = sum + val
print("\nSum of Fibonacci numbers =", sum)
