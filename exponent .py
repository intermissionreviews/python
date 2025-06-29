
def power(base: int, exponent: int) -> float:
    # if the exponent is zero then we should return 1 
    if exponent == 0:
        return 1 
        
# if the exponent is negative than convert it to a postive 
    if exponent < 0:
        base = 1 / base 
        exponent = -exponent

    results = 1 
    while exponent > 0:
    # check if the exponent is odd and multiply it by the results
        if exponent % 2 == 1: 
            results *= base
    
    #square the base
        base *= base
    
    #divide the exponet by 2
        exponent //= 2
    return results
print(power(2, 3)) 
    
    
    