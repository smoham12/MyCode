import matplotlib.pyplot as plt
import pandas as pd
import csv

# Exercise 1: Read Total profit of all months and show it using a line plot
def quest1(filePath):
    df = pd.read_csv(filePath, header=0)
    X = (df['month_number']).tolist()
    Y = (df['total_profit']).tolist()
    fig, ax = plt.subplots(1,1)
    fig.suptitle('Monthly profits')
    ax.plot(X, Y)
    ax.set_xlabel('Month')
    ax.set_ylabel('Profits')
    
    plt.show()
    return
    
#quest1('company_sales_data.csv')



# Exercise Question 2: Get Total profit of all months and 
# show line plot with the following Style properties
def quest2(filePath):
    df = pd.read_csv(filePath, header=0)
    X = df['month_number'].tolist()
    Y = df['total_profit'].tolist()
    fig, ax = plt.subplots(1,1)
    fig.suptitle('Total Profits')
    ax.plot(X,Y, color='r', lw=3, ls='--', marker='o')
    ax.set_xlabel("Month")
    ax.set_ylabel("Profits")
    
    plt.show()
    
#quest2('company_sales_data.csv')


# Exercise Question 3: Read all product sales data and show it  using a
# multiline plot
def quest3(filePath):
    df = pd.read_csv(filePath, header=0)
    monthsList      = df['month_number'].tolist()
    faceCreamList   = df['facecream'].tolist()
    faceWashList    = df['facewash'].tolist()
    toothpasteList  = df['toothpaste'].tolist()
    bathingSoapList = df['bathingsoap'].tolist()
    shampooList     = df['shampoo'].tolist()
    moisturizerList = df['moisturizer'].tolist()
    
    plt.plot(monthsList, faceCreamList, label = 'face cream', lw=3, marker='o')
    plt.plot(monthsList, faceWashList, label = 'face wash', lw=3, marker='o')
    plt.plot(monthsList, toothpasteList, label = 'toothpaste', lw=3, marker='o')
    plt.plot(monthsList, bathingSoapList, label = 'bath soap', lw=3, marker='o')
    plt.plot(monthsList, shampooList, label = 'shampoo', lw=3, marker='o')
    plt.plot(monthsList, moisturizerList, label = 'moisturizer',  lw=3, marker='o')
    
    plt.title('Sales data')
    plt.xlabel('Months')
    plt.ylabel('Sales Units')
    plt.legend()
    plt.show()
    return

#quest3('company_sales_data.csv')


# Exercise Question 4: Read toothpaste sales data 
# of each month and show it using a scatter plot
def quest5(filePath):
    df = pd.read_csv(filePath, header=0)
    X = df['month_number'].tolist()
    Y = df['toothpaste'].tolist()
    plt.scatter(X,Y, label='Toothpaste sales data')
    
    plt.title('Tooth Paste Sales Data')
    plt.legend(loc='upper left')
    plt.xlabel('Month Number')
    plt.ylabel('Nb units sold')
    plt.grid(b=True, axis='both', which='minor')
    plt.show()
    
    return

quest5('company_sales_data.csv')






















































