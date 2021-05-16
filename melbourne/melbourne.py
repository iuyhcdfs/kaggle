import pandas as pd

csvPath = './melb_data.csv'
data = pd.read_csv(csvPath)
data.describe()

