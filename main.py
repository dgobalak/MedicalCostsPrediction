import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def main(): 
    age = -1
    bmi = -1
    non_smoker = int(True)

    age = int(input("Enter age: "))
    bmi = float(input("Enter BMI: "))
    if input("Smoker? (y/n): ") == "y":
        non_smoker = int(False)

    pred = model.predict([[age, bmi, non_smoker]])
    print(pred)

if __name__ == '__main__':
    main()