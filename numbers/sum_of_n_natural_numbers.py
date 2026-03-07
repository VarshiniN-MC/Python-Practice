#Sum of n natural numbers
n=int(input("Enter the number : "))
sum=0
for i in range(n+1):
    sum=i+sum
print("The sum of ",n," Natural numbers is : ",sum)
