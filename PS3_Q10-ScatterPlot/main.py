#CSV reader reference: https://docs.python.org/3/library/csv.html
#line graph visualization reference: https://developers.google.com/chart/interactive/docs/gallery/scatterchart
import csv
from app import app
from flask import jsonify, request, render_template
#Creates a scatter plot the relationship between the total revenue earned by arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009		
@app.route('/google-charts/scatter-plot')
def google_pie_chart():
    File = open('static/arcade-revenue-vs-cs-doctorates.csv')
    Reader = csv.reader(File)
    #skips the header
    header = next(Reader)
    #Stores the data in a dictionary by removing the null rows
    dictOfItems = {rows[0]:[rows[1],rows[2]] for rows in Reader}
    File.close()
    return render_template('scatter-plot-copy.html', data=dictOfItems)

if __name__ == "__main__":
    app.run()