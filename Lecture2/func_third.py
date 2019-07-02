def Inner(New_Func,a):
    print("Inner Working!")
    New_Func(a)

def New_Func(a):
    print("New Func Working!")
    print(a)

def NewNew_Func(a):
    print("NewNewfUNC Working!")
    print(a*100)



Inner(New_Func,50)
Inner(NewNew_Func,50)




