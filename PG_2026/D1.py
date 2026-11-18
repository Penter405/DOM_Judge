amount=int(input())
d=list(map(int,input().split()))
total=sum(d)
average=total/len(d)
best=1#if all has 0
best_has=0
more=0
studentID=0
for student in d:
    studentID+=1
    if student>best_has:
        best_has=student
        best=studentID
    if (student*10**10)>=int(average*10**10):
        more+=1
    
print(total)
print(f"{average:.2f}")
print(best)
print(more)