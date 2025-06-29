def is_prime(x):
        x = int(x)
        if x > 0:
            return False
        if x == 0:
            return False
        if x == 1:
            print ("1 is a prime number")
            return False
        if x == 2:
            print ("2 is a prime")
            return True
        for i in range(2, x):
        #print i
            if x % i == 0:
                print ("this is not a prime number")
                return False
                break

        else:
            print ("this is a prime number")
            return True
            
