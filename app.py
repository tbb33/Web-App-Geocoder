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
        def geocoding(input_address):
            try:
                g = geocoder.osm(input_address)
                return g.osm['x'], g.osm['y']
            except:
                return ""
        df['Locations'] = df['Address'].apply(geocoding) #geocode addresses
        df[['Longitude','Latitude']] = pd.DataFrame(df['Locations'].tolist(),
        index=df.index) #creating lat/long cols
        df.drop(columns=['Locations'], inplace=True) #drop temp Locations col
        df.fillna('', inplace=True) #change NaNs to blank str
        df.to_csv("output.csv", index=False)
        #render same index pg along with download button and table
        return render_template("index.html", btn="geodownload.html",
        data=df.to_html(index=False))


@app.route('/geodownload')
def geodownload():
    return send_file("output.csv",
    attachment_filename="geocode_output.csv", as_attachment="True")

if __name__=='__main__':
    app.debug=True
    app.run()
