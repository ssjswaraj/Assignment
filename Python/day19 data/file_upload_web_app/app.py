from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = img.filename
                img.save(filename)
                msg = "Upload Done ! "
                return render_template("index.html",msg =msg)

if __name__ == "__main__":
    #app.run(host="0.0.0.0",port=8080) # EC2 on AWS
    app.run(host="127.0.0.1",port=8080) # local machine
    # app.run(host="172.25.12.70",port=8080) # local machine
    