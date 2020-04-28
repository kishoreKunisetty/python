t=int(input('enter the number of times you want to repeat it'))
for i in range(t):
    low=int(input('Enter the lower limt for this guess:'))
    high=int(input('Enter the upper limt for this guess:'))
    s="wrong"
    while s != "correct":
        m=int((low+high+1)/2)
        print(m)
        s=input('Enter it is \" low or high or correct\" for your guess number (consider camelcase):')
        if s == "low":
            low = m+1
        elif s == "correct":
            print(m," is your guess number")
        else :
            high = m-1
