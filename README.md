# Web-App-Geocoder
 
### This web app (deployed on local host) allows the user to upload a CSV file containing addresses in a column named "Address" (any case variation is allowed) and then download a new file (named geocode_output.csv) with 2 new columns (lat/long) containing the coordinates to those addresses. The new columns are appended to the end. 

Run this app by executing app.py and open local host on browser. 
<br>Note: You may need to install a local virtual environment for Python. You may need to install Flask. If this program is ran several times, you may need to clear your cache in order to download the newest file from the site.

I learned how to:
1. Independently create a web app - used Flask as Web Framework
2. Geocode using Geocoder and OpenStreetMap API (Nominatim Geocoding service is built on top of OpenStreetMap data)
   - Note: Google Maps API is much faster but not free
3. Stylze HTML page using Bootstrap library
4. Create upload/download feature
5. Edit CSV using reader and writer modules in Python
   - Later switched to using Pandas dataframes for simplicity - found this logic was much easier
7. Append new columns to the end

Files:
1. app.py: contains Python code to handle backend and make changes to CSV file
2. index.html (inside templates folder): HTML code stylized using Bootstrap
3. geodownload.html (inside templates folder): HTML code for download button feature
4. sample_input.csv: example of CSV file to upload to the web app
5. uploaded_sample_input.csv: example of file saved to computer when user clicks sumbit button - simply a copy of uploaded CSV
6. output.csv: example of file saved to computer when user clicks sumbit button - this is the new file containing lat/long columns and will be the same file available for user to download
