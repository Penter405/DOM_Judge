target,n=list(map(int,input().split()))
nums=list(map(int,input().split()))
p1=0
p2=0
all=nums[0]
result=0
now_len=1
while p2<len(nums) and p1<len(nums):
    #print(all==sum(nums[p1:p2+1]))
    if all<target:
        p2+=1
        if p2==len(nums):
            break
        all+=nums[p2]
        now_len+=1
        
    else:
        #all>=target
        if result==0 or now_len<result:
            result=now_len
        all-=nums[p1]
        now_len-=1
        p1+=1
print(result)