def Square(a):
    b=list()
    b.append(a[0])
    b.append(a[-1])
    return b
a=list(input())
print(Square(a))