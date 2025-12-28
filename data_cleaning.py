
import pandas as pd

def clean_dataframe(df):
    df = df.drop_duplicates()
    return df
