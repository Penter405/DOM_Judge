while True:
    try:
        d=input()
        print(d==d[::-1])
    except:
        exit()