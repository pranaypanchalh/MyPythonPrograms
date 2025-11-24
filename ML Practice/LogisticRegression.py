import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7],
    "Pass":  [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

x = df[['Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

hours = int(input('Enter Hours:'))
prediction = model.predict([[hours]])
probability = model.predict_proba([[hours]])

print(f"Prediction for {hours} hours: {prediction[0]}")
print(f"Probability of passing: {probability[0][1]}")

x_vals = np.linspace(0, 8, 100).reshape(-1, 1)
y_vals = model.predict_proba(x_vals)[:, 1]

plt.scatter(x, y, color="blue")
plt.plot(x_vals, y_vals, linewidth=3)
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression Sigmoid Curve")
plt.show()