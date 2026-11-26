for _ in range(int(input())):
    sizeof=int(input())
    *d,target=list(map(int,input().split()))
    ever=set()
    for node in d:
        could=target-node
        if could in ever:
            print("YES")
            break
        ever.add(node)
    else:
        print("NO")