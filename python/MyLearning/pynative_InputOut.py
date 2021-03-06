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
    
#quest5()


# Exercise Question 6: write all file content into new file by skiping 
# line 5 from following file
def quest6(lineIgnr):
    inp = open("test.txt", 'r')
    s = inp.readlines()
    out = open("NewFile.txt", "w")
    n = len(s)
    for i in range(lineIgnr-1):
        out.write(s[i])
    for i in range(lineIgnr, n):
        out.write(s[i])
    
    inp.close()
    out.close()
    return

quest6(5)   


# Exercise Question 7: Accept any three string from one input() call
def quest7():
    s = input("Enter 3 string: ")
    l = s.split()
    n = len(l)
    if(n!=3):
        print('You didnt enter 3 strings, you entered {0}'.format(n))
    else:
        for i in range(3):
            print(l[i])
        #end for i in range
    #
    
#quest7()


# Exercise Question 8: You have the following data.
# totalMoney = 1000
# quantity = 3
# price = 450
# display above data using string.format() method

def quest8():
    totalMoney = 1000
    quantity = 3
    price = 450
    outFile = open('money.txt','w')
    s = 'I have {0} dollars so I can buy {1} football ' \
          'for {2:.2f} dollars'.format(totalMoney,quantity,price)
    print(s)
    outFile.write(s)

#quest8()
    


# Exercise Question 10: Read line number 4 from the following file
def quest10():
    inp = open('test.txt', 'r')
    s = inp.readlines()
    rslt = s[3]
    print(rslt)
    
#quest10()
    