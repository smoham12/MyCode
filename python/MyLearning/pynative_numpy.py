import numpy as np

# Question 1: Create a 4X2 integer array and Prints its attributes
def quest1():
    a = np.array( np.zeros(shape=(4,2), dtype=int) )
    print('The shape of the array is: ', a.shape)
    print('The number of dimensions is: ', a.ndim)
    print('The item size is: ', a.itemsize)
    return
    
    
#quest1()

# Question 2: Create a 5X2 integer array from a range 
# between 100 to 200 such that the difference between each element is 10
def quest2():
    a = range(100, 200, 10)
    b = np.array(a)
    c = b.reshape((5,2))
    print(c)
    return

#quest2()

# Question 3: Following is the provided numPy array. return 
# array of items in the third column from all rows
def quest3():
    sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
    nbRows, nbCols = sampleArray.shape
    returnArray = (sampleArray[:, 2]).reshape(nbCols, 1)
    return returnArray

#print(quest3())




# Question 4: Following is the given numpy array return array 
# of odd rows and even columns
def quest4():
    sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], \
                    [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
    newArray= sampleArray[::2 , 1::2]
    print('Sample Array')
    print(sampleArray)
    print('New Array')
    print(newArray)

#quest4()


# Question 5: Add the following two NumPy arrays and Modify a result 
# array by calculating the square of each element
def quest5():
    arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
    arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
    
    arraySum = arrayOne + arrayTwo
    arraySq = np.square(arraySum)
    print('Addition of 2 arrays is:')
    print(arraySum)
    print('Square of result is:')
    print(arraySq)

#quest5()


# Question 6: Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 
# such that the difference between each element is 1 and then Split 
# the array into four equal-sized sub-arrays. 
def quest6():
    array = range(10,34,1)
    npArray = np.array(array)
    npArray = npArray.reshape((8,3))
    print(npArray)

# quest6()



# Question 8: Following is the 2-D array. Print max from axis 0 and min 
# from axis 1
def quest8():
    A = np.array([[34,43,73],[82,22,12],[53,94,66]])
    min0 = A.min(axis=0)
    min1 = A.min(axis=1)
    print('Array is:')
    print(A)
    print('Min x-axis:')
    print(min0)
    print('Min y-axis:')
    print(min1)
    return

quest8()

















