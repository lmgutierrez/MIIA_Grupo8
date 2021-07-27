#!/usr/bin/python
from flask import Flask, request
from m09_model_deployment import predict_proba

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def Pricepredict():
    return {
         "result": predict_proba(request.args.get('YEAR','MILEAGE','STATE', 'MAKE', 'MODEL'))
        }, 200


@app.route('/nombre', methods=['GET'])
def nombre():
    return {
         "Year": request.args.get('YEAR'),
         "Mileage": request.args.get('MILEAGE'),
         "State": request.args.get('STATE'),
         "Make": request.args.get('MAKE'),
          "Model": request.args.get('MODEL')          
        }, 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

