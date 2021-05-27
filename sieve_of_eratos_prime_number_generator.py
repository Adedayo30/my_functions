def sieve_of_eratos(num):
    """This function prints list of prime numbers between 2 and num(specified limit). 
    It is assumed you knew how Sieve of Erastosthenes technique works""" 
    #define the varaible prime_number that will hold the prime numbers
    prime_numbers = []
    #define the variable that holds 0s and 1s but it holds 1s at the initial stage
    ones_list = [1  for one in range(0, num)]
    #define the starting point
    x = 2
    y = 2

    #loop through specified limit. Get the multiples of 2 first
    while (x*y < num):
        ones_list[x*y] = 0 #1 at x*y(logically 2*2) is turned to 0
        # increament y. As you increament, 1 turns to 0
        y += 1   
        #when the limit is reached, increament x; the loop start again     
        if x*y >= num: 
            x += 1
            y = 2

    #Now get the equivalent position/index where 1 is not turned to 0
    for prime in range(2, num):
        if ones_list[prime] == 1:
            prime_numbers.append(prime)
    return prime_numbers

print('\n', sieve_of_eratos(50))
#print('\n', sieve_of_eratos(120))
#print('\n', sieve_of_eratos(150))