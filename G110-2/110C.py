result=[]
is_plus=1
while True:
    try:
        data=input().strip()
    except:
        break

    buffer=int(data[0])

    for rs in data[1:]:
        buffer+=int(rs)*is_plus
        is_plus*=-1
    result.append(str(buffer))

print("\n".join(result))

