#factorial of a number using recursion
def fact(n):
    if n==0 or n==1: 
        return 1
    else:
        return(n*fact(n-1))
n=int(input("Enter a positive integer:"))
print("Factorial of", n, "=", fact(n))
