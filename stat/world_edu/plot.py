import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

file = "\\1699460825-wide_2023_sept.csv"
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+file, "r") as f:
    df = pd.read_csv(f, index_col=0)

print(df.head())