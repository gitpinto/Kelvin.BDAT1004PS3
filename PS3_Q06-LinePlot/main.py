#CSV reader reference: https://docs.python.org/3/library/csv.html
#line graph visualization reference: https://developers.google.com/chart/interactive/docs/gallery/linechart
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a line graph showing the number of marriages and divorces per capita in the U.S. between 1867 and 2014		
@app.route('/google-charts/line-graph')
def google_pie_chart():
    File = open('static/us-marriages-divorces-1867-2014.csv')
    Reader = csv.reader(File)
    #skips the header
    header = next(Reader)
    #Stores the data in a dictionary by removing the null rows
    dictOfItems = {rows[0]:[rows[4],rows[5]] for rows in Reader if (rows[4] != '' or rows[5] != '')}
    File.close()
    return render_template('line-graph.html', data=dictOfItems)

if __name__ == "__main__":
    app.run()