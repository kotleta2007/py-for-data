from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
data = data.drop(columns=['Country', 'AverageTemperatureUncertainty', 'Latitude', 'Longitude'])

print(data)
