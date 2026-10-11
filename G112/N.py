"""
-1 2 -3 4 -5 6 -7
-1 1 -2 2


"""
def f(n):
    if n%2==0:
        return (n+1)//2
    return - ((n+1)//2)
print(f(int(input())))