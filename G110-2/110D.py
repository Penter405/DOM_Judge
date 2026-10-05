def get_ans():
    min_135=float("inf")

    useless=int(input())

    data=list(map(int,input().split()))
    if sum(data)%2==0:
        return sum(data)
    new=[rs for rs in data if rs %2!=0]
    return sum(data)-min(new)

print(get_ans())