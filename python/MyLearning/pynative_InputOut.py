# Exercise Question 1: Accept two numbers from the user and 
# calculate multiplication
def quest1():
    a = eval(input("Enter First Number: "))
    b = eval(input("Enter Second Number: "))
    print(a*b)
    
#quest1()


# Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” 
# using output formatting of a print() function
def quest2():
    print('My', 'Name', 'Is', 'James', sep='**')

#quest2()

# Exercise Question 3: Convert decimal number to octal using print() 
# output formatting
def quest3(x):
    print('{0:4d} in decimal is {1:4o} in Octal'.format(x,x) )
    return

#quest3(10)
 

#Exercise Question 4: Display float number with 2 decimal places using print()
def quest4(fltNb):
    print('{0:8.4f} with {1} dps is {2:8.2f} with {3} dps'.format(fltNb, 4, fltNb, 2))
    return

#quest4(458.541315)


# Exercise Question 5: Accept list of 5 float numbers as a input from user
def quest5():
    n = 5
    rslt = []
    for i in range(n):
        x = eval( input('Enter a float: ') )
        rslt.append(x)
    print(rslt)
    
quest5()
        