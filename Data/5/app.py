import data as dt

data = dt.data_import("../data/phone.csv")
# print(data[data["Price"] >= 150000000].sort_values("Price", ascending=False))
print(data["Price"].median(axis=0))
