#Binary Search
low=0
high=MAX-1
Key=int(input(“enter search key”))
while(low<=high):
        middle=int((low+high)/2)
        if(key==array[middle]):
     	 	print(“key found at position:”,middle)
           	 break        
        elif(key<array[middle]):
            high=middle-1
        else:
            low=middle+1;  
If(low>high):
	print(“key not found”)
