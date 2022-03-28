from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from csv import writer, reader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['POST']) #url
def success():
    global file
    file=request.files["file"]
    file.save(secure_filename("uploaded"+file.filename))

    with open("uploaded"+file.filename, "r") as read_file,\
    open("ooutput.csv", "w",newline='') as write_file:
        csv_reader = reader(read_file)
        csv_writer = writer(write_file)
        print(csv_reader.line_num)
        for row in csv_reader:
            #new column
            if csv_reader.line_num == 1: #header
                row.append("Latitude")
            else:
                row.append(row[0]+'a') #first row append "a"
            csv_writer.writerow(row)


    return render_template("index.html", btn="download.html") #shows index pg along with download button

@app.route('/download')
def download():
    return send_file("uploaded"+file.filename,
    attachment_filename="geocoded.csv", as_attachment="True")

if __name__=='__main__':
    app.debug=True
    app.run()
