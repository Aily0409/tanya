import math
factorial_numbers= (6,11,15,22)

for number in factorial_numbers:
    done_factorial= 1
    for i in range (1, number +1):
        done_factorial*= i
    print (done_factorial)  
    if done_factorial == math.factorial(number):
        print("Verified factorial")
        
def Remainder(divided, divisor):
    while divided >= divisor:
        divided-= divisor
    return divided

division_remainder= [(3, 2), (21, 4), (131, 19), (81, 9)]

for pair in division_remainder:
    divided, divisor= pair
    remainder_answer= Remainder(divided, divisor)
    print("Remainder of", divided,"/", divisor, "is" ,remainder_answer)    
         

