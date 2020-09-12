import numpy as np
import pandas as pd


# Question 1: From given data set print first and last five rows
def quest1():
    df = pd.read_csv('Automobile_data.csv', header=0)
    print(df.head())
    print(df.tail())
    return

quest1()