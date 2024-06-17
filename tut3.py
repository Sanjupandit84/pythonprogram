# x=int(input("enter the first number"))
# y=int(input("enter the first number"))

# def arithmeticOperation(x,y):
   
#    return x+y,x-y,x/y,x*y,x//y,x%y
#    x=int(input("enter number1"))
#    y=int(input("enter number2"))

# print(  arithmeticOperation(x,y))

   
# p=(arithmeticOperation(x,y)[0])
# q=(arithmeticOperation(x,y)[1])
# r=(arithmeticOperation(x,y)[2])
# s=(arithmeticOperation(x,y)[3])
# t=(arithmeticOperation(x,y)[4])
# u=(arithmeticOperation(x,y)[5])

# print(p)
# print(q)
# print(r)
# print(s)
# print(t)
# print(u)


x=int(input("enter first number"))
y=int(input("enter second number"))
a=(input("enter any operator"))


def calculator(x,y):
    if a=="+":
        print(x+y)
    elif a=="-":
        print(x-y)
    elif a=="*":
        print(x*y)
    elif a=="/":
        print(x/y)
    elif a=="//":
        print(x//y)
    elif a=="%":
        print(x%y)
    else:
        print("default value")
        return x+y, x-y, x*y, x/y, x//y, x%y
calculator(x,y)



