from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import csv
import pandas as pd
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/geocode', methods=['POST']) #url
def success():
    global file
    if request.method=='POST':
        file=request.files["file"] #get file from user
        file.save(secure_filename("uploaded_"+file.filename))
        df = pd.read_csv("uploaded_"+file.filename)
        #capitalize first letter, rest lowercase
        df.columns = [x.capitalize() for x in df.columns]
        print(df.columns)
        #addr_index = df.columns.get_loc("Address")
        #print(addr_index) #get col index
        #print(type(df))
        def geocoding(input_address):
            try:
                g = geocoder.osm(input_address)
                return g.osm['x'], g.osm['y']
            except:
                return ""
        #for row in df.iterrows():
        df['Locations'] = df['Address'].apply(geocoding)
        df[['Longitude','Latitude']] = pd.DataFrame(df['Locations'].tolist(),
            index=df.index)
        print(df)


        return render_template("index.html", btn="gdownload.html", data=df.to_html())

@app.route('/gdownload')
def gdownload():
    return send_file("output.csv",
    attachment_filename="geocoded_output.csv", as_attachment="True")

if __name__=='__main__':
    app.debug=True
    app.run()
