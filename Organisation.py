import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")

del df["Luminosity"]
del df["Unnamed: 0"]

print(df.shape)

df.to_csv("final.csv")