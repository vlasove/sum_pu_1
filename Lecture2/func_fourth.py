cur = 0.000000001

def MySqrt(a):
    x = 1
    c = 0
    while True:
        c+=1
        if abs(x - 1/2*(x+a/x)) < cur:
            print(x , c)
            break
        else:
            x = 1/2*(x+a/x)
        #print(x)

    return x



num = float(input())
print(MySqrt(num))
