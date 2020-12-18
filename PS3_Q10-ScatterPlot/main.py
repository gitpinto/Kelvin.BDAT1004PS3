#CSV reader reference: https://docs.python.org/3/library/csv.html
#line graph visualization reference: https://developers.google.com/chart/interactive/docs/gallery/linechart
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a pie chart for all the roman emperors who were assassinated. It a even circle and there are 22 records each with 4.5% in the pie chart		
@app.route('/google-charts/scatter-plot')
def google_pie_chart():
    File = open('static/arcade-revenue-vs-cs-doctorates.csv')
    Reader = csv.reader(File)
    #skips the header
    header = next(Reader)
    #Stores the data in a dictionary by removing the null rows
    dictOfItems = {rows[0]:[rows[1],rows[2]] for rows in Reader}
    # listYear = list(dictOfItems.keys())
    # listVal = list(dictOfItems.values())
    # count = len(listYear)
    # listRevenue = []
    # listDoctorates = []
    # for item in listVal:
    #     listRevenue.append(item[0])
    #     listDoctorates.append(item[1])

    # listData = [listYear, listRevenue, listDoctorates]
    # dictData = {listYear: [listRevenue, listDoctorates]}
    #Sorts the dictionary based on the kill count
    File.close()
    return render_template('scatter-plot-copy.html', data=dictOfItems)

if __name__ == "__main__":
    app.run()