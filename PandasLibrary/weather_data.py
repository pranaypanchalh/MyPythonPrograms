import csv
import pandas

"""with open ("PandasLibrary/weather_data.csv" , "r") as dataFile:
    data = csv.reader(dataFile)
    temprature = []
    for i,row in enumerate(data):
        if row[1] != "temp":
            temprature.append(int(row[1]))
    print(temprature)"""

data = pandas.read_csv("PandasLibrary/weather_data.csv")
print(data["temp"])
tempList = data["temp"].to_list()
print(data["temp"].max())

print(data[data.day == "Monday"])