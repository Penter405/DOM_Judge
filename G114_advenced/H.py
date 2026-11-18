data=list(map(int,input().split()[:-1]))
large=max(data)

factor=[0 for _ in range(large+1)]#skip index 0
for partner in range(1,large+1):
    for go_through in range(partner*2,large+1,partner):
        factor[go_through]+=partner


for guy in data:
    guy=int(guy)
    print("%5d" % guy,end=" ")
    if guy==factor[guy]:
        print("PERFECT")
    elif guy>factor[guy]:
        print("DEFICIENT")
    else:
        print("ABUNDANT")
    

