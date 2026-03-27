class Number:
    def __init__(self):
        pass
    @staticmethod
    def happy(num):
        appear=set()
        result=num
        #appear.add(result)
        buffer=0
        while result not in appear:
            appear.add(result)
            buffer=0
            for rs in str(result):
                buffer+=int(rs)**2
            result=buffer
            if result==1:
                return True


        return False
print(Number.happy(int(input())))