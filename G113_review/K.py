from decimal import Decimal, ROUND_HALF_UP
for _ in range(int(input())):
    d=Decimal(input())
    d=d.quantize(exp=Decimal('0.01'), rounding=ROUND_HALF_UP)
    res=f"{d:.2f}"
    if res=="-0.00":
        res="0.00"
    print(res)
"""
 |  quantize(self, /, exp, rounding=None, context=None)                                                                                                                                                            
 |      Return a value equal to the first operand after rounding and having the                                                                                                                                    
 |      exponent of the second operand.                                                                                                                                                                            
 |                                                                                                                                                                                                                 
 |          >>> Decimal('1.41421356').quantize(Decimal('1.000'))                                                                                                                                                   
 |          Decimal('1.414')                                                                                                                                                                                       
 |                                                                                                                                                                                                                 
 |      Unlike other operations, if the length of the coefficient after the quantize                                                                                                                               
 |      operation would be greater than precision, then an InvalidOperation is signaled.                                                                                                                           
 |      This guarantees that, unless there is an error condition, the quantized exponent                                                                                                                           
 |      is always equal to that of the right-hand operand.                                                                                                                                                         
 |                                                                                                                                                                                                                 
 |      Also unlike other operations, quantize never signals Underflow, even if the                                                                                                                                
 |      result is subnormal and inexact.                                                                                                                                                                           
 |                                                                                                                                                                                                                 
 |      If the exponent of the second operand is larger than that of the first, then                                                                                                                               
 |      rounding may be necessary. In this case, the rounding mode is determined by the                                                                                                                            
 |      rounding argument if given, else by the given context argument; if neither                                                                                                                                 
 |      argument is given, the rounding mode of the current thread's context is used.    
"""