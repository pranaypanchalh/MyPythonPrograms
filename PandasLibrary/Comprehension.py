import pandas as pd

studentDict = {
    "student":["Angela", "James", "Lily"],
    "score":[56,76,98]
}

studentDF = pd.DataFrame(studentDict)
print(studentDF)

for (index, row) in studentDF.iterrows():
    print(row.score)