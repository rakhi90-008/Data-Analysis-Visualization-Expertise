
import numpy as np

def basic_stats(series):
    return {
        "mean": series.mean(),
        "median": series.median(),
        "std": series.std()
    }
