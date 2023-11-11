import pandas as pd
from pandas import DataFrame

stat_data = pd.read_csv(
    r"/Users/rajvirsingh/Desktop/Personal Projects/HackTheChange2023/Binary-Brains-/co-emissions-per-capita.csv"
)

canada_stat_data = stat_data[stat_data["Entity"] == "Canada"]
pd.DataFrame(canada_stat_data)
canada_stat_data = canada_stat_data.iloc[216:222]

print(canada_stat_data)
