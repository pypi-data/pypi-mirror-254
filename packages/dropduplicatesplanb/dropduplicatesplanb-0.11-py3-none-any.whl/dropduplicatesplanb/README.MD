# Drops duplicates in DataFrames with tedious dtypes
 
## Tested against Windows / Python 3.11 / Anaconda

## pip install dropduplicatesplanb

```
import pandas as pd
from dropduplicatesplanb import pd_add_drop_duplicates_planB

pd_add_drop_duplicates_planB()
df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
)


df["baba"] = df.Embarked.apply(lambda q: [q, q, q, q])
df.loc[0, "baba"] = [[[1, 2, 34, 4, 2, 2, 34, 2, 1]]]
df.loc[1, "baba"] = [[[1, 2, 34, 4, 2, 2, 34, 2, 1]]]
df = pd.concat([df for x in range(2)], ignore_index=True)
df21 = df.d_drop_duplicates_planB(subset="baba")
df32 = df.d_drop_duplicates_planB(subset=["PassengerId", "Survived"])
df43 = df.d_drop_duplicates_planB(subset=["PassengerId", "Survived"], keep="first")
df54 = df.d_drop_duplicates_planB()
print(df)
print(df21)
print(df32)
print(df43)
print(df54)

```
