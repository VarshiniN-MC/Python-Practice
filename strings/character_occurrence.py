#To check number of occurrence of each character in the string using dictionary
str=input("Enter the words ")
dictionary={}
for i in str:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
       dictionary[i]=1
print("The number of occurrences are : ",dictionary)
