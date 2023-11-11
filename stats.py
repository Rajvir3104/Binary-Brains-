import pandas as pd
from pandas import DataFrame
import numpy as np


stat_data = pd.read_csv(
    r"/Users/rajvirsingh/Desktop/Personal Projects/HackTheChange2023/Binary-Brains-/co-emissions-per-capita.csv"
)

canada_stat_data = stat_data[stat_data["Entity"] == "Canada"]
pd.DataFrame(canada_stat_data)
canada_stat_data = canada_stat_data.iloc[216:222]

carbon_emissions = canada_stat_data["AnnualCO2Emissions"]
carbonCanada = np.array([carbon_emissions])
average_carbon_canada = carbonCanada.mean()


def point_system(total_personal_emission, average_carbon_canada):
    high_emissions = average_carbon_canada * 2
    score = int((total_personal_emission / high_emissions) * 100)
    if score > 99:
        score = "100+"

    return score
