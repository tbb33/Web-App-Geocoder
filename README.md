# Web-App-Geocoder
 
## This web app (deployed on local host) allows the user to upload a CSV file containing addresses in the 2nd column and then download a new file (named geocoded_output.csv) with 2 new columns  (lat/long) containing the coordinates to those addresses. The new columns are appended to the end. 

Run this app by executing app.py and open local host on browser. You may need to install a local virtual environment for Python. You may need to install Flask.

I learned how to:
1. Independently create a web app - used Flask as Web Framework
2. Geocode using OpenStreetMap API (Nominatim Geocoding service is built on top of OpenStreetMap data)
   - Note: Google Maps API is much faster but not free
3. Stylze HTML page using Bootstrap library
4. Create upload/download feature
5. Edit CSV using reader and writer modules in Python
6. Append new columns to the end

Files:
1. app.py: contains Python code to handle backend and make changes to CSV file
2. index.html (inside templates folder): HTML code stylized using Bootstrap
3. gdownload.html (inside templates folder): HTML code for download button feature
4. sample_input.csv: example of CSV file to upload to the web app
