for _ in range(int(input())):
    guys,least=list(map(int,input().split()))
    d=list(map(int,input().split()))
    d.sort(key= lambda x:-x)
    did=0
    picked=0
    for guy in d:
        picked+=1
        if picked*guy>=least:
            did+=1
            picked=0
    print(did)
"""
3
5 10
7 11 2 9 5
4 8
2 4 2 3
4 11
1 3 3 7
"""