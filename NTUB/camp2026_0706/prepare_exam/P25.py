a="700602"
data=input().split()
get_0=[4,3,10]
for rs in range(3):
    a+=data[rs].zfill(get_0[rs])

buffer=0
is_7=0
for rs in a:
    if is_7:
        buffer+=int(rs)*7
        is_7=0
    else:
        buffer+=int(rs)
        is_7=1
print(buffer%10)