while True:
    try:
        d=input()
    except:
        break
    print(d==d[::-1])