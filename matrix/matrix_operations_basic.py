#Matrix Operations without numpy

#1.addition & substraction without numpy
mm1= input("Enter Matrix 1 value (4 numbers) :")
mm2= input("Enter Matrix 2 value (4 numbers) :")
a, b, c, d = mm1.split()
e, f, g, h = mm2.split()

m1=[[int(a),int(b)],[int(c),int(d)]]
m2=[[int(e),int(f)],[int(g),int(h)]]
m3=[[0,0],[0,0]]
m4=[[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j]=m1[i][j] + m2[i][j]
        m4[i][j]=m1[i][j] - m2[i][j]
print("Addition of matrix: ", m3)
print("Substraction of matrix: ",m4)

#2.equal or not
found=1
for i in range(0,2):
    for j in range(0,2):
        if m1[i][j] !=m2[i][j]:
            found=0
if found==1:
    print("equal ")
else:
    print("not equal")

#3. transpose
t=[[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2): 
        t[j][i]=m1[i][j]
print("original matrix1 :",m1)
print("transpose matrix1 :",t)
        
            
