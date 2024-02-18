import pandas as pd
import numpy as np


def minutesToSeconds(column):
    column = pd.to_numeric(column) / 60
    return column


def showHeaders(df):
    headers = []
    for col in df.columns:                                               
        headers.append(col)
    return headers      


def convertToExcel(df, file_path):
    df.to_excel(file_path, index=False, engine='openpyxl')


def addHeaders(df, column_list):
    df.columns = column_list
    return df


def addTestTime(df, start_time, increment):
    num_rows = len(df)                                 # Number of rows present in the dataset

    df['Test Time'] = np.linspace(start_time, start_time + (num_rows - 1) * increment, num_rows)
    return df


def dataSmoothing(column):
    window_size = 800  
    column = column.rolling(window=window_size).mean().dropna()
    return column


def parse_solution_to_df(solution):
    columns = ["Voltage [V]", "Current [A]", "Time [s]"]
    df = pd.DataFrame({column: solution[column].data for column in columns})
    return df