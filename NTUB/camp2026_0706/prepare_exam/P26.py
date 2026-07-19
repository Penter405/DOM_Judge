#dp is saving result of a sub question
#find whats same in the climb stair:
"""
in fibonassi, our goal is fiding result of it, so we save every fib(n) result.
"""

"""
f(n)=sigma i=1-3( f(i) )
and the returning of function should be the total way 


"""



"""
can solve every problem in a math equaltion
define the meaning of function return
and get the equaltion
remember who is the stop recursion sign, and put it in the front
"""
dp=dict()

def recursion(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n in dp:
        return dp[n]
    buffer=0
    for rs in range(1,4):
        buffer+=recursion(n-rs)
    dp[n]=buffer
    return buffer
print(recursion(int(input())))