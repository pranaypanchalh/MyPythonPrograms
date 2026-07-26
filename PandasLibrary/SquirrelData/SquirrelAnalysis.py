import pandas as pd

data = pd.read_csv("PandasLibrary/SquirrelData/SquirrelData.csv")
graySquirrelsCount = len(data[data["Primary Fur Color"] == "Gray"])
redSquirrelsCount = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackSquirrelsCount = len(data[data["Primary Fur Color"] == "Black"])
print(graySquirrelsCount, redSquirrelsCount, blackSquirrelsCount)

dataDict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[graySquirrelsCount,redSquirrelsCount,blackSquirrelsCount]
}

df = pd.DataFrame(dataDict)
df.to_csv("PandasLibrary/SquirrelData/SquirrelCount.csv")