import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Age":[2,5,3,7,1],
    "Kms_Driven":[25000,60000,40000,90000,15000],
    "Engine_CC":[1200,1500,1300,1800,1000],
    "Resale_Price":[650000,420000,520000,300000,720000]
}

df = pd.DataFrame(data)

X = df[["Age","Kms_Driven","Engine_CC"]]
y = df["Resale_Price"]

model = LinearRegression()
model.fit(X,y)

age = int(input("Enter Age: "))
kms = int(input("Enter Kms Driven: "))
engine = int(input("Enter Engine CC: "))

price = model.predict([[age,kms,engine]])

print("Estimated Resale Price =", price[0])
