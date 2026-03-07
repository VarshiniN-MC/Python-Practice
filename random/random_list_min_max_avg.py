#Find average, maximum, minimum of a random list
import random
L=[]
for i in range(10):
    l=random.randint(1,10)
    L.append(l)
print("List",L)
print("Minimum",min(L))
print("Maximum",max(L))
sum=0
for i in L:
    sum=i+sum
avg=sum/10
print("Average",avg)

