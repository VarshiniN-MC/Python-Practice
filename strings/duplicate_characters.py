#Check the duplicated and not duplicated characters
str=input("Enter the words ")
duplicate=[]
nondup=[]
#loop for duplicated characters
for i in str:
    if str.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print("The duplicated characters are : ",duplicate)
#loop for not duplicated characters
for j in str:
    if j not in duplicate:
        nondup.append(j)
print("Not duplicated characters are : ",nondup)
