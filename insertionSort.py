if __name__=="__main__":
    a=[]
    n=int(input('enter the number of numbers you want to sort:'))
    print('enter the numbers')
    for i in range(n):
        a.append(int(input()))
    for i in range(len(a)):
        key = a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    print(a)
