#CSV reader reference: https://docs.python.org/3/library/csv.html
#Pie-chart visualization reference: https://developers.google.com/chart/interactive/docs/gallery/piechart and class notes
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a pie chart for all the roman emperors who were assassinated. It a even circle and there are 22 records each with 4.5% in the pie chart	

#Creates a pie chart for the count of cause of death
@app.route('/google-charts/pie-chart')
def google_pie_chart_count():
    File = open('static/roman-emperor-reigns.csv')
    Reader = csv.reader(File)
    header = next(Reader)
    dictOfItems = {rows[0]:rows[2] for rows in Reader}
    listOfItems = []
    for key in dictOfItems.keys():
        listOfItems.append(dictOfItems[key])
    dictOfCount = {'Cause_of_Death' : 'Count'}
    for i in listOfItems:
        dictOfCount[i] = listOfItems.count(i)
    File.close()
    return render_template('pie-chart.html', data=dictOfCount)
		
if __name__ == "__main__":
    app.run()