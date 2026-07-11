"""
7, 7, 10, 10, 10, 4, 2

"""
#print()
data=list(map(int,input().split(", ")))
#s=[1,2,3]
#print(s[:-2])
data=(sorted(data)[2:-2])
print(int((sum(data)//len(data))//1))
