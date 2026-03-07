#takes the length of a list, generates random numbers list, and gives odd & even numbers
import random
n=int(input("enter the length of list"))
L=[]
for i in range(n):
    l=random.randint(1,1000)
    if l not in L: 
        L.append(l)
print("List of random numbers",L)
even=[]
odd=[]
for j in L:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("Even numbers from the random list : ",even)
print("Odd numbers from the random list :",odd)
        
        
