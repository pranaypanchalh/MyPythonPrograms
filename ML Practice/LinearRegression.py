import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 50, 55, 60, 65, 70, 75, 80]
}
df = pd.DataFrame(data)

x = df[['Hours']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

hours = int(input("Enter Hours:"))
predicted_marks = model.predict([[hours]])
print(f"Predicted marks for studying {hours} hours = {predicted_marks[0]}")

'''plt.scatter(x, y)                       # scatter plot of actual data
plt.plot(x, model.predict(x), linewidth=3)  # regression line
plt.xlabel("Hours studied")
plt.ylabel("Marks scored")
plt.title("Linear Regression Example")
plt.show()'''
