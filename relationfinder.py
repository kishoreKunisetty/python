def net(a,b):
        return [a*b, a/b, a+b, a-b]
def layer1(a,b):
    layer=net(a,b)
    return layer
def layer2(l,n,number):
    countouter=0
    for i in l:
        countouter+=1
        if i<number:
            if i*n==number:
                return [countouter,1]
            elif i+n==number:
                return [countouter,3]
            else :
                pass
        else :
            if i/n==number:
                return [countouter,2]
            elif i-n==number:
                return [countouter,4]
            else :
                pass
    return [countouter,0]
def char(arg):
    switcher={
        1:"*",
        2:"/",
        3:"+",
        4:"-",
    }
    return switcher[arg]
def main():
    a=int(input('enter number1:'))
    b=int(input('enter number2:'))
    c=int(input('enter number3:'))
    n=int(input('enter output:'))
    w=layer1(a,b)
    i=layer2(w,c,n)
    if 0 in i:
        print("relation cannot be generated")
    else:
        print(a,char(i[0]),b,char(i[1]),c,"=",n)
main()



if __name__=='__main__':
    print('enter 5 numbers so that you can find arthamatic relations amoung them :')
    n1=int(input(''))
    n2=int(input(''))#1:+ 2:- 3:* 4:/
    n3=int(input(''))
    n4=int(input(''))
    n5=int(input(''))
    result=0
    if n1+n2+n3+n4==n5:
        print(n1,'+', n2,'+', n3,'+', n4,'=', n5)
    elif n1+n2+n3-n4==n5:
        print(n1,'+', n2,'+', n3,'-', n4,'=', n5)
    elif n1+n2+n3*n4==n5:
        print(n1,'+', n2,'+', n3,'*', n4,'=', n5)
    elif n1+n2+n3/n4==n5:
        print(n1,'+', n2,'+', n3,'/', n4,'=', n5)
    elif n1+n2-n3+n4==n5:
        print(n1,'+', n2,'-', n3,'+', n4,'=', n5)
    elif n1+n2-n3-n4==n5:
        print(n1,'+', n2,'-', n3,'-', n4,'=', n5)
    elif n1+n2-n3*n4==n5:
        print(n1,'+', n2,'-', n3,'*', n4,'=', n5)
    elif n1+n2-n3/n4==n5:
        print(n1,'+', n2,'-', n3,'/', n4,'=', n5)
    elif n1+n2*n3+n4==n5:
        print(n1,'+', n2,'*', n3,'+', n4,'=', n5)
    elif n1+n2*n3-n4==n5:
        print(n1,'+', n2,'*', n3,'-', n4,'=', n5)
    elif n1+n2*n3*n4==n5:
        print(n1,'+', n2,'*', n3,'*', n4,'=', n5)
    elif n1+n2*n3/n4==n5:
        print(n1,'+', n2,'*', n3,'/', n4,'=', n5)
    elif n1+n2/n3+n4==n5:
        print(n1,'+', n2,'/', n3,'+', n4,'=', n5)
    elif n1+n2/n3-n4==n5:
        print(n1,'+', n2,'/', n3,'-', n4,'=', n5)
    elif n1+n2/n3*n4==n5:
        print(n1,'+', n2,'/', n3,'*', n4,'=', n5)
    elif n1+n2/n3/n4==n5:
        print(n1,'+', n2,'/', n3,'/', n4,'=', n5)
    elif n1-n2+n3+n4==n5:
        print(n1, '-', n2,'+', n3,'+', n4,'=', n5)
    elif n1-n2+n3-n4==n5:
        print(n1,'-', n2,'+', n3,'-', n4,'=', n5)
    elif n1-n2+n3*n4==n5:
        print(n1,'-', n2,'+', n3,'*', n4,'=', n5)
    elif n1-n2+n3/n4==n5:
        print(n1,'-', n2,'+', n3,'/', n4,'=', n5)
    elif n1-n2-n3+n4==n5:
        print(n1,'-', n2,'-', n3,'+', n4,'=', n5)
    elif n1-n2-n3-n4==n5:
        print(n1,'-', n2,'-', n3,'-', n4,'=', n5)
    elif n1-n2-n3*n4==n5:
        print(n1,'-', n2,'-', n3,'*', n4,'=', n5)
    elif n1-n2-n3/n4==n5:
        print(n1,'-', n2,'-', n3,'/', n4,'=', n5)
    elif n1-n2*n3+n4==n5:
        print(n1,'-', n2,'*', n3,'+', n4,'=', n5)
    elif n1-n2*n3-n4==n5:
        print(n1,'-', n2,'*', n3,'-', n4,'=', n5)
    elif n1-n2*n3*n4==n5:
        print(n1,'-', n2,'*', n3,'*', n4,'=', n5)
    elif n1-n2*n3/n4==n5:
        print(n1,'-', n2,'*', n3,'/', n4,'=', n5)
    elif n1-n2/n3+n4==n5:
        print(n1,'-', n2,'/', n3,'+', n4,'=', n5)
    elif n1-n2/n3-n4==n5:
        print(n1,'-', n2,'/', n3,'-', n4,'=', n5)
    elif n1-n2/n3*n4==n5:
        print(n1,'-', n2,'/', n3,'*', n4,'=', n5)
    elif n1-n2/n3/n4==n5:
        print(n1,'-', n2,'/', n3,'/', n4,'=', n5)
    elif n1*n2+n3+n4==n5:
        print(n1, '*', n2,'+', n3,'+', n4,'=', n5)
    elif n1*n2+n3-n4==n5:
        print(n1,'*', n2,'+', n3,'-', n4,'=', n5)
    elif n1*n2+n3*n4==n5:
        print(n1,'*', n2,'+', n3,'*', n4,'=', n5)
    elif n1*n2+n3/n4==n5:
        print(n1,'*', n2,'+', n3,'/', n4,'=', n5)
    elif n1*n2-n3+n4==n5:
        print(n1,'*', n2,'-', n3,'+', n4,'=', n5)
    elif n1*n2-n3-n4==n5:
        print(n1,'*', n2,'-', n3,'-', n4,'=', n5)
    elif n1*n2-n3*n4==n5:
        print(n1,'*', n2,'-', n3,'*', n4,'=', n5)
    elif n1*n2-n3/n4==n5:
        print(n1,'*', n2,'-', n3,'/', n4,'=', n5)
    elif n1*n2*n3+n4==n5:
        print(n1,'*', n2,'*', n3,'+', n4,'=', n5)
    elif n1*n2*n3-n4==n5:
        print(n1,'*', n2,'*', n3,'-', n4,'=', n5)
    elif n1*n2*n3*n4==n5:
        print(n1,'*', n2,'*', n3,'*', n4,'=', n5)
    elif n1*n2*n3/n4==n5:
        print(n1,'*', n2,'*', n3,'/', n4,'=', n5)
    elif n1*n2/n3+n4==n5:
        print(n1,'*', n2,'/', n3,'+', n4,'=', n5)
    elif n1*n2/n3-n4==n5:
        print(n1,'*', n2,'/', n3,'-', n4,'=', n5)
    elif n1*n2/n3*n4==n5:
        print(n1,'*', n2,'/', n3,'*', n4,'=', n5)
    elif n1*n2/n3/n4==n5:
        print(n1,'*', n2,'/', n3,'/', n4,'=', n5)
    elif n1/n2+n3+n4==n5:
        print(n1, '/', n2,'+', n3,'+', n4,'=', n5)
    elif n1/n2+n3-n4==n5:
        print(n1,'/', n2,'+', n3,'-', n4,'=', n5)
    elif n1/n2+n3*n4==n5:
        print(n1,'/', n2,'+', n3,'*', n4,'=', n5)
    elif n1/n2+n3/n4==n5:
        print(n1,'/', n2,'+', n3,'/', n4,'=', n5)
    elif n1/n2-n3+n4==n5:
        print(n1,'/', n2,'-', n3,'+', n4,'=', n5)
    elif n1/n2-n3-n4==n5:
        print(n1,'/', n2,'-', n3,'-', n4,'=', n5)
    elif n1/n2-n3*n4==n5:
        print(n1,'/', n2,'-', n3,'*', n4,'=', n5)
    elif n1/n2-n3/n4==n5:
        print(n1,'/', n2,'-', n3,'/', n4,'=', n5)
    elif n1/n2*n3+n4==n5:
        print(n1,'/', n2,'*', n3,'+', n4,'=', n5)
    elif n1/n2*n3-n4==n5:
        print(n1,'/', n2,'*', n3,'-', n4,'=', n5)
    elif n1/n2*n3*n4==n5:
        print(n1,'/', n2,'*', n3,'*', n4,'=', n5)
    elif n1/n2*n3/n4==n5:
        print(n1,'/', n2,'*', n3,'/', n4,'=', n5)
    elif n1/n2/n3+n4==n5:
        print(n1,'/', n2,'/', n3,'+', n4,'=', n5)
    elif n1/n2/n3-n4==n5:
        print(n1,'/', n2,'/', n3,'-', n4,'=', n5)
    elif n1/n2/n3*n4==n5:
        print(n1,'/', n2,'/', n3,'*', n4,'=', n5)
    elif n1/n2/n3/n4==n5:
        print(n1,'/', n2,'/', n3,'/', n4,'=', n5)
    else:
        print('relation not satisfied.')
