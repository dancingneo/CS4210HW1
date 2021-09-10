#-------------------------------------------------------------------------
# AUTHOR: Wan Suk Lim
# FILENAME: find_s.py
# SPECIFICATION: find-s algorithm
# FOR: CS 4210- Assignment #1
# TIME SPENT: 30 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv fil
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
for i in db:
    if i[4] == 'Yes':
        hypothesis = i
        break

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
for i in db:
    if i[4] == 'Yes':
        if i[0] != hypothesis[0]:
            hypothesis[0] = '?'
        if i[1] != hypothesis[1]:
            hypothesis[1] = '?'
        if i[2] != hypothesis[2]:
            hypothesis[2] = '?'
        if i[3] != hypothesis[3]:
            hypothesis[3] = '?'


hypothesis.pop()
print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)