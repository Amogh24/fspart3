import torch
import pandas as pd;
from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.nn.functional as F
df = pd.read_csv("C:/Users/amogh/Downloads/diabetes.csv")
print(df.head())
feature_cols = [ 'Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure','Pregnancies']
x = df[feature_cols]
y = df.Outcome
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state=1)
X_train = torch.FloatTensor(X_train.values)
X_test = torch.FloatTensor(X_test.values)
Y_train = torch.LongTensor(Y_train.values)
Y_test = torch.LongTensor(Y_test)

class Linear(nn.Module):
  def __init__(self):
     super().__init__()
     self.fc1 = nn.Linear(6,80)
     self.fc2 = nn.Linear(80,20)
    
     self.fc3 = nn.Linear(20,1)
   
  def forward(self,x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    
    x = (self.fc3(x))
    
    return (x)
model = Linear()
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.01)

def binary_acc(y_pred, y_test):
    y_pred_tag = torch.round(torch.sigmoid(y_pred))

    correct_results_sum = (y_pred_tag == y_test).sum().float()
    acc = correct_results_sum/y_test.shape[0]
    acc = torch.round(acc * 100)
    
    return acc

epochs = 350
for i in range(epochs):
  optimizer.zero_grad()
   
  predictions = (model(X_train))
  Y_train = Y_train.float()
  predictions = predictions.view(-1)
  acc = binary_acc(predictions,Y_train)
  loss = criterion(predictions,Y_train)
  
  loss.backward()
  optimizer.step()
#   if i%10 == 0:
#     print("Loss = {} |Accuracy = {}".format(loss,acc))

with torch.no_grad():
  predictions = (model(X_test))
  Y_test = Y_test.float()
  predictions = predictions.view(-1)
  acc = binary_acc(predictions,Y_test)
  print("accuracy = {}%".format(acc))


  def run(params):
    arr = []
    arr.append(params['insulin'])
    arr.append(params['bmi'])
    arr.append(params['glucose'])
    arr.append(params['bp'])
    arr.append(params['pregnancies'])
    arr.append(params['age'])
    arr = torch.FloatTensor(arr)
    prediction = model(arr)
    prediction = prediction.view(-1)
    tag = torch.round(torch.sigmoid(prediction))
    return tag
