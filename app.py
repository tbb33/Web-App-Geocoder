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
    # with open("uploaded"+file.filename, "w") as output:
    #     output.write("Test")
    with open("uploaded"+file.filename, "r") as read_file,\
    open("ooutput.csv", "w",newline='') as write_file:
        csv_reader = reader(read_file)
        csv_writer = writer(write_file)
        for row in csv_reader:
            row.append("Test")
            csv_writer.writerow(row)
            # row_count = sum(1 for row in read_file)
            # print(row_count)
            # print(row)

    return render_template("index.html", btn="download.html") #shows index pg along with download button

@app.route('/download')
def download():
    return send_file("uploaded"+file.filename,
    attachment_filename="geocoded.csv", as_attachment="True")

if __name__=='__main__':
    app.debug=True
    app.run()
