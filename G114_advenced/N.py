while True:
    try:
        d_size, want=list(map(int,input().split()))
    except:
        break
    data=list(map(int,input().split()))
    now=result=sum(data[:want])
    left=0
    right=want-1
    while right+1<d_size:
        right+=1
        now+=data[right]
        now-=data[left]
        result=max(result,now)
        left+=1

    print(result)
"""
9 2
-7 9 4 8 8 -6 5 -8 3

"""