import pandas as pd


df = pd.read_csv("big-mac-full-index.csv")
df.head()

### Index Method
# for index in df.index:
#     print(df['iso_a3'][index],
#           df['name'][index])

### Iterrows Method
for i,r in df.iterrows():
    print(r['iso_a3'],
          r['name'])

### Apply Method
print(df.apply(lambda row: row['iso_a3'], axis = 1))