a = [1,2,3,9,8,7,6]
for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]         #swap
print(a)
