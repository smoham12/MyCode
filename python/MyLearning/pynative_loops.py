# Exercise Question 1: Print First 10 natural numbers using while loop
def quest1(n):
    if (n<0):
        print('n must be > 0')
        return
    i=0
    while i<=n :
        print(i)
        i += 1
    #wend
    return

#quest1(10)


# Exercise Question 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
def quest2(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end= ' ')
        # for j
        print('')
    # for i


#quest2(10)


# Exercise Question 6: Given a number count the total number of digits in a number
def quest6(value):
    n=0 #nb digits
    
    
    
    while ( value/10  > 0 ):
        value = value - (value%10)
        value = value / 10
        n = n+1
    #wend
        
    print(n)
    
quest6(75856)