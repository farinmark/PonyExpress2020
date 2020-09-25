def Square(a):
    b=list()
    b.append(a*4)
    b.append(a*a)
    b.append(a*(2**(1/2)))
    return b
a=int(input())
print(Square(a))