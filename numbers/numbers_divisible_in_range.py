#takes a range and a number, then prints numbers in that range divisible by that number
start=int(input("Enter the starting range : "))
end=int(input("Enter the ending range : "))
number=int(input("Enter the number : " ))
if end<start:
    print("Error : value of starting number cannot be greater than ending number")
else:
    print("The numbers divisible by ",number,"in range(",start,",",end,") are :")
    for i in range(start,end+1):
        if i%number==0:
            print(i)
    
