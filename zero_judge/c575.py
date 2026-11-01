import bisect
want_wifi, wifi_service_point = list(map(int,input().split()))
want_wifi_points= list(map(int,input().split()))
want_wifi_points.sort()
left=0
distance=want_wifi_points[-1]-want_wifi_points[0]
right=(distance)
def find_rightest_legal(n,left=0,right=want_wifi-1):
    while left<=right:
        mid=(left+right+1)//2
        if want_wifi_points[mid]<=n:
            left=mid+1
        elif want_wifi_points[mid]>n:
            right=mid-1
    return right
find_rightest_legal(7)
def legal(r2):
    r=r2/2
    used_service_ind=-1
    for servicing in range(wifi_service_point):
        if used_service_ind+1>=want_wifi:
            return True
        used_service_ind+=1
        place=want_wifi_points[used_service_ind]+r
        fetch=place+r
        may_fetch=find_rightest_legal(fetch)
        used_service_ind=may_fetch
    return used_service_ind+1>=want_wifi
        

while left<=right:
    #we are finding min
    mid=(left+right+1)//2
    if legal(mid):
        right=mid-1
    else:
        left=mid+1
print(left)