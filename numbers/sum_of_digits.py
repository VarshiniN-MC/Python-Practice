#sum of digits
num=int(input("Enter the number : "))
sum=0
while num!=0:
  digit=num%10
  sum=digit+sum
  num=num//10
print("Sum of the digits is ",sum)
