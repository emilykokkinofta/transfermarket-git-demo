import pandas as pd

transfers = pd.read_csv("data/transfers.csv")

club_spending = (transfers
    .dropna(subset=["transfer_fee"])
    .groupby("to_club_name")["transfer_fee"]
    .sum()
    .sort_values(ascending = False)
    .head(10)
)

print(club_spending)