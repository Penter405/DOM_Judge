a,b,c=list(map(int,input().split()))
a2,b2,c2=list(map(int,input().split()))
n=int(input())
profit=float("-inf")
for fa in range(n+1):
    fb=n-fa
    now=a*fa*fa+b*fa+c+a2*fb*fb+b2*fb+c2
    profit=max(profit,now)

print(profit)