def reverse():
    rev=""
    for i in str:
        rev=i+rev
    return rev
str=input()
rev= reverse()
print(rev)
if rev==str:
    print("palindrome")
else:
    print("not palindrome")
