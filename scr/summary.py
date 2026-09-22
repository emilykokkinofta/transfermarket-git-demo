import pandas as pd

transfers= pd.read_csv("data/transfers.csv")

print(f"Number of transfers: {len(transfers)}")