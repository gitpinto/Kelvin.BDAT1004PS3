#CSV reader reference: https://docs.python.org/3/library/csv.html
#line graph visualization reference: https://developers.google.com/chart/interactive/docs/gallery/linechart
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a pie chart for all the roman emperors who were assassinated. It a even circle and there are 22 records each with 4.5% in the pie chart		
@app.route('/google-charts/horizontal-bar-graph')
def google_pie_chart():
    File = open('static/actor_kill_counts.csv')
    Reader = csv.reader(File)
    #skips the header
    header = next(Reader)
    #Stores the data in a dictionary by removing the null rows
    dictOfItems = {rows[0]:rows[1] for rows in Reader}
    #Sorts the dictionary based on the kill count
    sortedDictValues = sorted(dictOfItems.values())
    sortedDict = {}
    for i in sortedDictValues:
        for j in dictOfItems.keys():
            if dictOfItems[j] == i:
                sortedDict[j] = dictOfItems[j]
    File.close()
    return render_template('horizontal-bar-graph.html', data=sortedDict)

if __name__ == "__main__":
    app.run()