n=input()
dup=[]
non=[]
for i in n:
    if n.count(i)>1:
        if i not in dup:
            dup.append(i)
    else :
        non.append(i)
all=dup+non
print(all)
