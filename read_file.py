import pandas as pd


def read_file_csv(name_file):
    df = pd.read_csv(name_file)

    return df



df = read_file_csv('username.csv')
df.head()