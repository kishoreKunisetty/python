n=int(input('Enter the size of the list : '))
a=[]
for i in range(n):
    b=int(input('Enter the value in of this posision'))
    a.append(b)
print('the input list is')
print(a)
for i in range(len(a)):
    minInd = i
    for j in range(i,len(a),1):
        if a[j]<a[minInd]:
            minInd=j
    tmep = a[i]
    a[i]= a[minInd]
    a[minInd] = tmep
print('the sorted list is :')
print(a)
