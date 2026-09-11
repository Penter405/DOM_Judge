def get():
    m,r,r,n=list(map(int,input().split(",")))
    a=[list(map(int,input().split())) for _ in range(m)]
    b=[list(map(int,input().split())) for _ in range(r)]
    ab=[list(map(int,input().split()))for _ in range(m)]

    b=list(zip(*b))

    for a_col in range(m):
        for r_b_row in range(n):
            a_times_b=0
            state=1
            bad_r_col=-1#reversed or just correct
            his_friend=-1
            total=0
            any_9999=0
            for rs in range(r):
                if (a[a_col][rs]==9999 or  b[r_b_row][rs]==9999) and (a[a_col][rs]==0 or  b[r_b_row][rs]==0):
                    state=0
                    break
                if (a[a_col][rs]==9999 or  b[r_b_row][rs]==9999):
                    any_9999=1
                    bad_r_col=rs
                    if a[a_col][rs]==9999:
                        his_friend=b[r_b_row][rs]
                    else:
                        his_friend=a[a_col][rs]
                else:
                    total+=a[a_col][rs]*b[r_b_row][rs]
                

            if any_9999==0:
                continue
            if state==0:
                continue
            return (ab[a_col][r_b_row]-total)//his_friend



result=[]
for _ in range(int(input())):
    result.append(str(get()))

print("\n".join(result))