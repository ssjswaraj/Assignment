from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/') #index or landing page of website
def home():
    return render_template('index.html')
# 127.0.0.1:8080/predict
@app.route('/addition',methods=['POST']) #post method is used to send parameters in http request
def addition():
    '''
    For rendering results on HTML GUI'''
    try:
       int_features = [int(x) for x in request.form.values()]
       print("Features are ", int_features, " No of features =", len(int_features))
       prediction = sum(int_features)
       output = round(prediction, 2)
    except:
        output = "Some Error while calculation"
    # output =10
    return render_template('index.html', output_number='Sum of Inputs is {}'
        .format(output))


if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=8080) # EC2 on AWS
    app.run(host="127.0.0.1",port=8080) # local machine