a = []
for i in range(1,101):
    a.append(i)

b = a
c = a

def IsPifagor(a1,b1,c1):
    if a1**2 + b1**2 == c1**2 or b1**2+c1**2 == a1**2 or c1**2 + a1**2 == b1**2:
        return True
    else:
        return False

#def IsTriangle(a1,b1,c1):
#    if .....:
#        return True
#    else:
#        return False

counter = 0
for i in a:
    for j in b:
        for k in c:
            if IsPifagor(i,j,k):
                counter +=1

print(counter)
