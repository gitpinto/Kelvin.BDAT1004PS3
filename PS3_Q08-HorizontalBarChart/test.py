import csv

File = open('static/actor_kill_counts.csv')
Reader = csv.reader(File)
header = next(Reader)

dictOfItems = {rows[0]:rows[1] for rows in Reader}
sortedDictValues = sorted(dictOfItems.values())
sortedDict = {}
for i in sortedDictValues:
    for j in dictOfItems.keys():
        if dictOfItems[j] == i:
            sortedDict[j] = dictOfItems[j]

#dictOfItems.pop()
#print(dictOfItems)
#dictOfItems.items()
#list1 = list(dictOfItems.items())
#print(list1)
#res = [[key] + val for key, val in dictOfItems.items()] 
#res = {k: v for k, v in dictOfItems.items() if v[0] is not None}
print(sortedDict)
# S
    # if dictOfItems[key] == 'Assassinated':
    #     listOfItems.append(key)
# dictOfCount = {'Cause_of_Death' : 'Count'}
# for i in listOfItems:
#     dictOfCount[i] = listOfItems.count(i)
# #dictOfCount = {i:listOfItems.count(i) for i in listOfItems}
File.close()
# #print(dictOfItems)
#print(listOfItems)
# print(dictOfCount)