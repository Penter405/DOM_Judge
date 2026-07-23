def is_letter(x):
    if 'A'<=str(x)<='Z' or 'a'<=str(x)<='z':
        return 1
    return 0
for x in [1,'x','@']:
    print(is_letter(x))
exit()
s="123"
for rs in range(len(s)):
    for pe in range(rs+1,len(s)+1):
        print(s[rs:pe])