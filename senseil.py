from sklearn import datasets, svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import csv
import numpy
import random

#loading train dataset using csv

filename = 'training.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)

filename1 = 'train_y.csv'
raw_data1 = open(filename1, 'rt')
reader1 = csv.reader(raw_data1, delimiter=',', quoting=csv.QUOTE_NONE)

scaler = StandardScaler()
train_x = (scaler.fit_transform(list(reader)[1:]))

train_y = list(reader1)[1:]

print("Training....")

x, y = train_x, train_y


clf = svm.SVC(C=7120.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=6.191, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

clf.fit(x, y) 

print("Training Completed!")

filename2 = 'sorted_test.csv'
raw_data2 = open(filename, 'rt')
reader2 = csv.reader(raw_data2, delimiter=',', quoting=csv.QUOTE_NONE)

filename3 = 'test_y.csv'
raw_data3 = open(filename1, 'rt')
reader3 = csv.reader(raw_data3, delimiter=',', quoting=csv.QUOTE_NONE)

test_x = list(reader2)[1:]
test_y = list(reader3)[1:]

#Determining accuracy on test data
print(clf.predict(test_x[0:]))
print('------------------------------')
print("Accuracy of algorithm: "+ str(round(accuracy_score(clf.predict(test_x[0:]), test_y[0:])*100, 1)) + " %")


from twilio.rest import Client as twi   #importing this to allow us to create a Twilio Client object capable of sending messages between phone numbers

acc_sid="AC581386961962cc5d454db9cba850e705"

auth_token="ca4be4ff7462d5658b40bacfe821c891"

client=twi(acc_sid,auth_token)      #Client object called client created here

while True:
    
    soil = []
    soil1 = []
    ca = float(input("Enter calcium content: "))
    soil.append(ca)
    p = float(input("Enter phosphorus content: "))
    soil.append(p)
    ph = float(input("Enter pH value: "))
    soil.append(ph)
    soc  = float(input("Enter soc value: "))
    soil.append(soc)
    sand = float(input("Enter sand value: "))
    soil.append(sand)
    soil1.append(soil)


    if(clf.predict(soil1[0:]) == '0'):
        print(clf.predict(soil1[0:]))
        print("Erodable")

    else:
        print(clf.predict(soil1[0:]))
        print("Good to go")
