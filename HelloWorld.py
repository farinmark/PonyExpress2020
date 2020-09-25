def Square(a):
    k=int()
    for i in a:
        k=0
        for j in a:
            if i==j:
                k=k+1
        if k>1:
            return "yes"
    return "no"
a=list(input())
print(Square(a))