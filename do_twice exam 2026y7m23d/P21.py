def not_na(x):
    if x<0:
        return -x
    return x

x,y =list(map(int,input().split()))
mx,my =list(map(int,input().split()))
print(not_na(mx)+not_na(my)+not_na(mx-(-x))+not_na(my-(-y)))