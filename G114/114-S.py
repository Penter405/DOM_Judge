res=[]


def find_parent(n):
    if n==parent[n]:
        return n
    return find_parent(parent[n])
def get_res():
    global parent
    edge=[]
    already=0
    for _ in range(way):
        a,b,w=list(map(int,input().split()))
        already+=w
        edge.append((w,a,b))
    edge.sort()
    res=0
    did=0# ==city-1 -> result

    for w,a,b in edge:
        if did>=city-1:
            return already-res
        if not(find_parent(a)==find_parent(b)):
            #not loop
            res+=w
            parent[find_parent(b)]=find_parent(a)
            did+=1
    return already-res

for _ in range(int(input())):
    city,way=list(map(int,input().split()))
    parent=[n for n in range(city)]
    res.append(get_res())

for rs in res:
    print(rs)

"""
3
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
3 3
0 1 5
1 2 5
2 0 10
4 3
0 1 5
1 2 5
2 3 5


"""
        

    
