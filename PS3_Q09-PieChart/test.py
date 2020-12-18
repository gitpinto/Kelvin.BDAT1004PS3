import csv

File = open('static/roman-emperor-reigns.csv')
Reader = csv.reader(File)
header = next(Reader)
dictOfItems = {rows[0]:rows[2] for rows in Reader}

listOfItems = []
for key in dictOfItems.keys():
    #listOfItems.append(dictOfItems[key])
    if dictOfItems[key] == 'Assassinated':
        listOfItems.append(key)
dictOfCount = {'Cause_of_Death' : 'Count'}
for i in listOfItems:
    dictOfCount[i] = listOfItems.count(i)
#dictOfCount = {i:listOfItems.count(i) for i in listOfItems}
File.close()
#print(dictOfItems)
print(listOfItems)
print(dictOfCount)