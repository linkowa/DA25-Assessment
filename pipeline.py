import requests
import pandas as pd


# Extract: make a GET request to the API and fetch the data
url = "https://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(url).json()


# Transform data to a Pandas DataFrame
df = pd.DataFrame.from_dict(response)


# Load
df.to_csv("makeup_data.csv")