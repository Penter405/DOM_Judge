"""permutaion_of_node_amount=[1,1]
biggest=20
for ind in range(2,biggest+1):
    permutaion_of_node_amount.append(ind*permutaion_of_node_amount[])
"""
def p(x,y):
    res=1
    for i in range(y):
        res*=(x-i)
    return res

def catalan(n):
    return ( p(n*2,n)// p(n,n)  ) //(n+1)
res=[]
for _ in range(int(input())):
    d=int(input())
    if d%2==0:
        res.append(0)
    else:
        res.append((catalan(d//2)))

for rs in res:
    print(rs)
    


"""
C 5 of 3= p5 of 3 / (3 guy order)
=p5 of 3 / p3 of 3
p x to y
times(i=0, i<y)-> x-i
"""