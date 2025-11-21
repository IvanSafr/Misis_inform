from math import factorial, e

 
x = 0.1

h = 0.005

b = 1

while x <= b:
    
    print(f"\nx = {x}")
    
    sum = 0

    i = 0

    val = 0.0001

    while abs(val) >= 0.0001:

        val = (x**(2*i) / (factorial(2*i)))

        sum += val        
        
        print(f'При i = {i} значение = {val}  сумма {sum} (e^x + e^(-x)) / 2 = {(e**x + e**(x*(-1)))/2}')
    
        i += 1
       
    x = round((x + h), 4)

