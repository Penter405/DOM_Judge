result=[]
for _ in range(int(input())):
    data=input().split(":")
    if data[0]=="00":
        result.append(f"12:{(str(data[1])).zfill(2)} AM")
    elif data[0]=="12":
        result.append(f"12:{(str(data[1])).zfill(2)} PM")
    elif int(data[0])>12:
        result.append(f"{(str(int(data[0])-12)).zfill(2)}:{(str(data[1])).zfill(2)} PM")
    else:
        result.append(f"{(str(data[0])).zfill(2)}:{(str(data[1])).zfill(2)} AM")
print("\n".join(result))