have={
    "T":4,
    "C":6,
    "O":8,
    "D":12,
    "I":20
}
res=0
for _ in range(int(input())):
    res+=have[input()[0]]

print(res)
