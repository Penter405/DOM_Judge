wow=set(['a', 'o', 'y', 'e', 'u', 'i'])
d=['']
for char in input().lower():
    if char not in wow:
        d.append(char)

print('.'.join(d))