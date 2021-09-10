#-------------------------------------------------------------------------
# AUTHOR: Wan Suk Lim
# FILENAME: decision_tree.py
# SPECIFICATION:decision tree
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
a= int(1)
b= int(1)
c= int(1)
d= int(1)
dict = {}
if db:
    for i, row in enumerate(db):
        temp = []
        for j, ele in enumerate(row):
            #print("i: " ,i, " j: ", j)
            if j == 4:
                X.append(temp)
                continue
            if ele in dict:
                temp.append(dict[ele])
            else:
                if(j == 0):
                    dict[ele]=a
                    temp.append(dict[ele])
                    a=a+1
                elif (j == 1):
                    dict[ele]=b
                    temp.append(dict[ele])
                    b = b + 1
                elif (j == 2):
                    dict[ele]=c
                    temp.append(dict[ele])
                    c = c + 1
                elif (j == 3):
                    dict[ele]=d
                    temp.append(dict[ele])
                    d = d + 1

#print(dict)
#print(X)

# X =

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
e= int(1)
dictY = {}
if db:
    for i, row in enumerate(db):
        if row[4] in dictY:
            Y.append(dictY[row[4]])
        else:
            dictY[row[4]]=e
            Y.append(dictY[row[4]])
            e=e+1

#print(Y)
# Y =

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()