# Question 1: Given a two integer numbers return their product and 
# if the product is greater than 1000, then return their sum
def quest1(a, b):
    return_prod = a*b
    if return_prod > 1000 :
        return (a+b)
    else:
        return return_prod
    
#a = 40
#b = 30
#print(quest1(a,b))



# Question 2: Given a range of first 10 numbers, Iterate from start number to 
# the end number and print the sum of the current number and previous number
def quest2():
    n = 10
    prior = 0
    run_sum = 0
    print("Priting current and previous number sum in a given range(", n, ")")
    for i in range(n):
        run_sum = i + prior
        print("Current Number", i, "Previous Number", prior, "Sum:", run_sum)
        prior = i
    #end for i in range
        
#quest2()


# Question 3: Given a string, display only those characters which are 
# present at an even index number.
def quest3(s):
    n = len(s)
    for i in range(0, n, 2):
            print(s[i])
        #end if (i%2)
    #end for i

#str = "pynative"
#quest3(str)


# Question 4: Given a string and an integer number n, 
# remove characters from a string starting from zero up to n 
# and return a new string
def quest4(s,n):
    return(s[n:])

#str = "pynative"
#print(quest4(str,4))


