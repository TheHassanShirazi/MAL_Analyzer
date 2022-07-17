import pandas as pd
from collections import Counter
from statistics import mean
import pprint

data_to_pull = input("What do you want to sort by? ").lower()

df = pd.read_excel('AnimeList.xlsm', sheet_name="Sheet2")
df = df.fillna('')

count = 0
countprinter = 0
studios = {}
datapull = {
    "name": 0,
    "media": 9,
    "season": 12,
    "studio": 14
}

column = datapull[data_to_pull]

while count < len(df.index):
    var = df.iloc[:, column].str.split("[")[count][0]

    if var == '':
        print("skip")
    else:
        item = df.iloc[:, column].str.split("[")[count][0]

        if item in studios:
            studios[item] = round(mean([studios[item], df.iloc[count, 4]]), 3)
        else:
            studios[item] = df.iloc[count, 4]
    if count % 100 == 0:
        countprinter += 1
        print("Now done " + str(countprinter * 100))
    else:
        pass
    count += 1


studios_sorted = {k: v for k, v in reversed(sorted(studios.items(), key=lambda x: x[1]))}

pprint.pprint(studios_sorted, sort_dicts=False)
