#Sum of the numbers untill 0 is entered
sum=0
while True:
    n=int(input("enter number to be added : "))
    if n==0:
        break
    else:
        sum=sum+n
print("The sum of the numbers is : ",sum)
    
