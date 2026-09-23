import pandas as pd

transfers = pd.read_csv("data/transfers.csv")

top_transfers = (
    transfers.dropna(subset = ["transfer_fee"])
    .sort_values("transfer_fee",ascending=False)
    .head(10)
)

print(
    top_transfers[[ "player_name", "from_club_name","to_club_name","transfer_fee",]]
)