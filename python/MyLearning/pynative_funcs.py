# Exercise Question 3: Write a function calculation() such that it can 
# accept two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

def quest3(x, y):
    a1,a2 = x+y, x-y
    return (a1, a2)

#print (quest3(10, 6))


# Exercise Question 4: Create a function showEmployee() in such a way that it 
# should accept employee name, and it’s salary and display both, and if the 
# salary is missing in function call it should show it as 9000

def quest4(name, salary = 9000):
    print('Employee {0} salary is: {1}'.format(name, salary))

#quest4('Ben', 9000)





# Exercise Question 6: Write a recursive function to calculate the 
# sum of numbers from 0 to 10
def quest6(n):
    if n<0:
        print('Nb must be > 0')
        return
    if n ==0:
        return 0
    
    return ( n + quest6(n-1) )

#print(quest6(10))


# Exercise Question 8: Generate a Python list of all the even numbers 
# between 4 to 30

def quest8(start, end):
    if start > end :
        print('Second nb must be larger than first')
        return
    
    l = []
    if( (start%2) == 1 ):
        start = start+1
    for i in range(start, end, 2):
        l.append(i)
    return l

print(quest8(4,30))