#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv

myFile = "myFirstCSV.csv"
fieldNames = []
rows = []

with open(myFile,"r") as data:
    readData = csv.reader(data)
    fieldNames = next(readData)
    for everyData in readData:
        print(everyData)
        rows.append(everyData)

print(fieldNames)
print(rows)


# In[3]:


import csv

myFile = "myFirstCSV.csv"
fieldNames = ["Name","Age","Grade","Year From","Year To"]
rows = [["Shivansh","12","7","2020","2021"],["Vivaan","13","7","2020","2021"],["Kanishk","12","7","2020","2021"],["Sahib","12","7","2020","2021"]]

with open(myFile,"w") as data:
    writeData = csv.writer(data)
    writeData.writerow(fieldNames)
    writeData.writerows(rows)


# In[7]:


import csv

fieldNames =["Name","RollNo.","Class"] 
rows = [{"Name":"Shivansh","RollNo.":21,"Class":7},{"Name":"Vivaan","RollNo.":22,"Class":7},{"Name":"Kanishk","RollNo.":25,"Class":7}]
newRow = []
with open("classData.csv","w") as myData:
    writeData = csv.writer(myData)
    writeData.writerow(fieldNames)
    for element in rows:#This is the loop for every element (dict) in rows list
        newRow.append(element["Name"])#Here we append all the keys into the newRow
        newRow.append(element["RollNo."])
        newRow.append(element["Class"])
        writeData.writerow(newRow)#Here we write that row into the csv file
        newRow = []#Here we empty that row for new values
         


# In[10]:


import csv

fieldNames =["Name","RollNo.","Class"] 
rows = [{"Name":"Shivansh","RollNo.":21,"Class":7},{"Name":"Vivaan","RollNo.":22,"Class":7},{"Name":"Kanishk","RollNo.":25,"Class":7}]
with open("classData.csv","w") as data:
    writeData = csv.DictWriter(data,fieldnames = fieldNames)#This is the DictWriter which takes 2 arguements => the data object and fieldNames
    writeData.writeheader()#This is the method to add the fieldnames
    writeData.writerows(rows)#This is for writing the rows


# In[2]:


import csv

with open("intoCSV.csv","w") as data:
    writeData = csv.writer(data)
    fromText = open("fromText.txt","r")
    fieldNames = fromText.readline().split()
    writeData.writerow(fieldNames)
    rowone = []
    rows = []
    for i in range (0,3):
        rowone = fromText.readline().split()
        rows.append(rowone)
    writeData.writerows(rows)


# In[ ]:




