# Web-App-Geocoder

## General Info
 This web app (deployed on local host) allows the user to upload a CSV file containing addresses in a column named "Address" (not case-sensitive) and then download a new file (named geocode_output.csv) with 2 new columns (lat/long) containing the coordinates to those addresses. The new columns are appended to the end. 


## Setup
Run this app by executing app.py and open local host on browser. 
<br>Note: You may need to install a local virtual environment for Python. You may need to install Flask. If this program is ran several times, you may need to clear your cache in order to download the newest file from the site.

## What I learned
1. Independently create a web app - used Flask as Web Framework
2. Geocode using Geocoder and OpenStreetMap API (Nominatim Geocoding service is built on top of OpenStreetMap data)
   - Note: Google Maps API is much faster but not free
3. Stylze HTML page using Bootstrap library
   - First used CSS then Bootstrap for easier design
5. Create upload/download feature
6. Edit CSV using Pandas dataframe 
   - First used reader and writer modules in Python - found Pandas df was much easier
7. Append new columns to the end, replace NaN with blank strings
8. Use Jinja to display items
9. Display df table on web page

## Files
1. app.py: contains Python code to handle backend (i.e. make changes to CSV file and dataframe, geocode address)
2. index.html (inside templates folder): HTML code for page stylized using Bootstrap
3. geodownload.html (inside templates folder): HTML code for download button feature
4. sample_input.csv: example of CSV file to upload to the web app
5. uploaded_sample_input.csv: example of file saved to computer when user clicks sumbit button - simply a copy of uploaded CSV
6. output.csv: example of file saved to computer when user clicks sumbit button - this is the new file containing lat/long columns and will be the same file available for user to download
