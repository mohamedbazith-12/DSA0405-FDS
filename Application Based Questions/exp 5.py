import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

data = {
    "Income":[45000,30000,60000,28000,52000],
    "Credit_Score":[720,650,780,620,710],
    "Existing_Loans":[0,1,0,2,1],
    "Approved":[1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df[["Income","Credit_Score","Existing_Loans"]]
y = df["Approved"]

model = DecisionTreeClassifier()
model.fit(X,y)

income = int(input("Enter Income: "))
credit = int(input("Enter Credit Score: "))
loan = int(input("Enter Existing Loans: "))

prediction = model.predict([[income,credit,loan]])

if prediction[0]==1:
    print("Loan Approved")
else:
    print("Loan Rejected")

print("\nDecision Rules:")
print(export_text(model, feature_names=list(X.columns)))
