#Matix Addition and Subtraction without numpy
m1 = [[7, 5],[11, 13]]
m2 = [[6, 28],[10, 3]]
result = [[0, 0],[0, 0]]

#Martix elements
print("The elements of the first matrix are:")
for i in m1 :
    print(i)
print("The elements of the second matrix are:")
for i in m2 :
    print(i)

#Marix addition
print("Addition of two matrices: ")
for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[i][j] + m2[i][j]
for i in result:
    print(i)
    
#Martix substraction
print("Subtraction of two matrices: ")
for i in range(len(m1)):
    for c in range(len(m1[0])):
        result[i][j] = m1[i][j] - m2[i][j]
for i in result:
    print(i)
