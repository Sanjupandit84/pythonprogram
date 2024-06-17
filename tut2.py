# prt/100
p= float(input("enter the amount of p"))
r= float(input("enter the amount of r"))
t= float(input("enter the amount of t"))
def interestRate(p,r,t):
    si = p*r*t/100
    return si,p*2

simple_intrest =  interestRate(p,r,t)
print(round(simple_intrest[0],2))
print(round(simple_intrest[1],2))



