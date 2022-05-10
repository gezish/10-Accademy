import numpy as np
import pandas as pd

def convert_to_string(df, columns):
    for col in columns:
        df[col] = df[col].astype("string")

def convert_to_numbers(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col])

def convert_to_int(df, columns):
    for col in columns:
        df[col] = df[col].astype("int64")

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])

def multiply_by_factor(df, columns, factor):
    for col in columns:
        df[col] = df[col] * factor

def percent_missing_values(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")
