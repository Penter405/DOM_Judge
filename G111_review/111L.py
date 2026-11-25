now=input()
ban=set(input())
print(''.join([n for n in now if n not in ban]))