date=[]
def search(target):#find left is bigger or same as me
    left=0
    right=len(date)-1
    while left<=right:
        mid=(left+right)//2
        if date[mid]==target:
            return mid
        if date[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return left-1

s="""水瓶座: Aquarius, 1/21 ∼ 2/19
雙魚座: Pisces, 2/20 ∼ 3/20
牡羊座: Aries, 3/21 ∼ 4/20
金牛座: Taurus, 4/21 ∼ 5/21
雙子座: Gemini, 5/22 ∼ 6/21
巨蟹座: Cancer, 6/22 ∼ 7/22
獅子座: Leo, 7/23 ∼ 8/21
處女座: Virgo, 8/22 ∼ 9/23
天秤座: Libra, 9/24 ∼ 10/23
天蠍座: Scorpio, 10/24 ∼ 11/22
射手座: Sagittarius, 11/23 ∼ 12/22
摩羯座: Capricorn, 12/23 ∼ 1/20""".split("\n")
name=[]
for rs in s:
    rs=rs.replace(" ","").split(":")[1]
    a,b=rs.split(",")
    name.append(a)
    b,c=b.split("∼")
    b=b.split("/")
    b[0]=b[0].zfill(2)
    b[1]=b[1].zfill(2)
    date.append("".join(b))
res=[]
for _ in range(int(input())):
    b=input().split("/")
    b[0]=b[0].zfill(2)
    b[1]=b[1].zfill(2)
    res.append(search(("".join(b))))

for rs in res:
    print(name[rs])
