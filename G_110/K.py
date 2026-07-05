result=[]
while True:
    try:
        a=int(input())
        b=int(input())
        c=int(input())
        result.append(str(pow(a,b,c)))
        useless=input()
    except:
        break
print("\n".join(result))

"""dp={}#tuple(num,c) => result
primes=[]
#Num **isup mod c== (Num mod c)**isup
#make ** ==1 only
def solve(num,c):
    ans=1
    for rs in primes:
        if num<c:
            break
        if rs<c:
            continue
        ups=0
        while num%rs==0:
            ups+=1
            num//=rs
        ans*=(rs%c)**ups
    
        
    return ans*(num%c)

def make_prime_table():
    prime_list=[True]*100000
    prime_list[0]=False
    prime_list[1]=False
    for rs in range(100000):
        if prime_list[rs]==1:
            primes.append(rs)
            for pe in range(rs**2,100000,rs):
                prime_list[pe]=False

    



make_prime_table()
result=[]
while True:
    try:
        number=int(input())
        isup=int(input())
        c=int(input())
    except:
        break
    result.append(str(solve(number,c)**isup))

print("\n".join(result))

"""