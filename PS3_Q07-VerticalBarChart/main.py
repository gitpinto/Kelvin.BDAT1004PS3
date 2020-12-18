#CSV reader reference: https://docs.python.org/3/library/csv.html
#line graph visualization reference: https://developers.google.com/chart/interactive/docs/gallery/linechart
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a pie chart for all the roman emperors who were assassinated. It a even circle and there are 22 records each with 4.5% in the pie chart		
@app.route('/google-charts/vertical-bar-graph')
def google_pie_chart():
    File = open('static/us-marriages-divorces-1867-2014.csv')
    Reader = csv.reader(File)
    #skips the header
    header = next(Reader)
    #Stores the data in a dictionary by removing the null rows
    dictOfItems = {rows[0]:[rows[4],rows[5]] for rows in Reader if (rows[0] == '1900' or rows[0] == '1950' or rows[0] == '2000') }
    File.close()
    return render_template('vertical-bar-graph.html', data=dictOfItems)

if __name__ == "__main__":
    app.run()