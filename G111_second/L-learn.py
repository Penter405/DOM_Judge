def search_left(data,target):#if  no match element, find first bigger than us
    left=0
    right=len(data)-1
    #find left-> near left
    while left<=right:
        mid=(left+right)//2
        if data[mid]>=target:
            right= mid-1
        elif data[mid]<target:
            left=mid+1
    return left

"""
array=[1,7,2,6]
see 1  memo=[1] # we got 1 at last of subsequence of a length 1 array
see 7  memo=[1,7] # we find out 7 can be in front of 1 that 1 is a last occur element of subsequence
see 2  memo=[1,2] #we find 2 can be in front of 1, and 2 smaller than 7, 
 means they both can be in front of 1, but 2 is better, 
 so we saved 2, every >2 can be in front of 2, rather than >7. (so we have more chance if choosing 2)
see 6  memo=[1,2,6] # see, if we didnot pick up samller, 6 cant pick up memo=[1,7], but we can now let 6, (which is bigger than 2) be joined to this memo
"""


res=[]
for _ in range(int(input())):
    d=eval(input())
    d.sort(key= lambda item:(item[0],-item[1]))
    #print(d)
    memo=[]#index=size, value=best last occur integer in this length
    for _,b in d:
        good_place=search_left(memo,b)
        if good_place>len(memo)-1:
            memo.append(b)
        else:
            memo[good_place]=b
    res.append(len(memo))

for rs in res:
    print(rs)

"""
[[1,3],[1,4],[3,5],[3,4],[0,1]]
"""