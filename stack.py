#stack is LiFo
a=[]
def push(element):
    a.append(element)
def pop():
    if len(a)<0:
        print('stack is empty.')
    else :
        a.pop()
def display():
    for i in range(len(a)-1,-1,-1):
        print(a[i])
def main():
    element=int(input('number:'))
    push(element)
    display()
main()
