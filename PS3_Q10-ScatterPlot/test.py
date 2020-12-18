import csv

File = open('static/arcade-revenue-vs-cs-doctorates.csv')
Reader = csv.reader(File)
header = next(Reader)

dictOfItems = {rows[0]:[rows[1],rows[2]] for rows in Reader}
listYear = list(dictOfItems.keys())
listVal = list(dictOfItems.values())
count = len(listYear)
listRevenue = []
listDoctorates = []
for item in listVal:
    listRevenue.append(item[0])
    listDoctorates.append(item[1])

listData = [listYear, listRevenue, listDoctorates]
#dictData = {listYear: [listRevenue, listDoctorates]}
dictData = {listYear[i]:[listRevenue[i],listDoctorates[i]] for i in range(count)}
#dictOfItems.pop()
#print(dictOfItems)
#dictOfItems.items()
#list1 = list(dictOfItems.items())
#print(list1)
#res = [[key] + val for key, val in dictOfItems.items()] 
#res = {k: v for k, v in dictOfItems.items() if v[0] is not None}
# print(listYear)
# print(listRevenue)
# print(listDoctorates)
print(dictData)
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