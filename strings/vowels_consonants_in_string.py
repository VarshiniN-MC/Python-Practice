#List the vowels and consonants in a string
n=input()
v=[]
c=[]
for i in n:
    if i in "aeiouAEIOU":
        if i not in v:
            v.append(i)
    else:
        if i not in c:
            c.append(i)
print("list of vowels",v)
print("list of consonants",c)
        
