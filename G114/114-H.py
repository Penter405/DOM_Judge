win={
    "B":"T",
    "T":"C",
    "C":"W",
    "W":"B"
}
a,b=input().split()
if a==b:
    print(0)
else:
    if win[a]==b:
        print(1)
    elif win[b]==a:
        print(2)
    else:
        print(0)