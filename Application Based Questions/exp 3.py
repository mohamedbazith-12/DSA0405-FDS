import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Num_Links":[1,6,0,4,2],
    "Num_Caps_Words":[3,15,1,10,5],
    "Email_Length":[120,300,80,250,160],
    "Spam":[0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Num_Links","Num_Caps_Words","Email_Length"]]
y = df["Spam"]

model = LogisticRegression()
model.fit(X,y)

links = int(input("Enter Number of Links: "))
caps = int(input("Enter Capital Words: "))
length = int(input("Enter Email Length: "))

prediction = model.predict([[links,caps,length]])

print("Prediction:", prediction[0])
