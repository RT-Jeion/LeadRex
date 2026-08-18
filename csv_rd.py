import pandas as pd

dt1 = pd.read_csv("csv_files/sheet1.csv")
dt2 = pd.read_csv("csv_files/sheet2.csv")

i = 0
emails = dt1["emails"]

for email in emails:
    email = list(email)
    print(email)
    i += 1
    if i == 20:
        break
