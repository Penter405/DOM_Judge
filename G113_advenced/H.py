"""水瓶座: Aquarius, 1/21 ∼ 2/19
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
摩羯座: Capricorn, 12/23 ∼ 1/20"""
"""
name=[]
d=d.replace(" ","").split("\n")
out=[]
for c in d:
    a,b=c.split(",")
    a=a.split(":")
    name.append(a[1])
    bot=b.split("∼")[0].split("/")
    bot[0]=bot[0].zfill(2)
    bot[1]=bot[1].zfill(2)
    out.append("".join(bot))
print(name)
"""
from bisect import bisect_left
date=['0121', '0220', '0321', '0421', '0522', '0622', '0723', '0822', '0924', '1024', '1123', '1223']
name=['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']
res=[]

for _ in range(int(input())):
    me=input().split("/")
    me[0]=me[0].zfill(2)
    me[1]=me[1].zfill(2)

    place=bisect_left(date,"".join(me))
    if date[place]!="".join(me):
        place-=1
    res.append(name[place])
print("\n".join(res))