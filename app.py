from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from csv import writer, reader
import urllib
import requests
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/geocode', methods=['POST']) #url
def success():
    global file
    file=request.files["file"]
    #saves copy of uploaded file
    file.save(secure_filename("uploaded_"+file.filename))

    with open("uploaded_"+file.filename, "r") as read_file,\
    open("output.csv", "w",newline='') as write_file:
        csv_reader = reader(read_file)
        csv_writer = writer(write_file)

        for row in csv_reader:
            #lat column
            if csv_reader.line_num == 1: #header
                row.append("Latitude")
            else:
                url = 'https://nominatim.openstreetmap.org/search/' \
                + urllib.parse.quote(row[1]) +'?format=json'
                response = requests.get(url).json()
                if(len(response)!=0):
                    row.append(response[0]['lat'])
                else:
                    row.append("")
            #long column
            if csv_reader.line_num == 1: #header
                row.append("Longitude")
            else:
                url = 'https://nominatim.openstreetmap.org/search/' \
                + urllib.parse.quote(row[1]) +'?format=json'
                response = requests.get(url).json()
                if(len(response)!=0):
                    row.append(response[0]['lon'])
                else:
                    row.append("")
            csv_writer.writerow(row)
    #shows index pg along with download button
        return render_template("index.html", btn="gdownload.html")

@app.route('/gdownload')
def gdownload():
    return send_file("output.csv",
    attachment_filename="geocoded_output.csv", as_attachment="True")

if __name__=='__main__':
    app.debug=True
    app.run()
