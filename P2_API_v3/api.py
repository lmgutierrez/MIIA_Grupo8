#!/usr/bin/python
from flask import Flask, request
from model_deployment import predict_proba

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def nombre():
    return {
         "Year": request.args.get('Year'),
         "Mileage": request.args.get('Mileage'),
         "State": request.args.get('State'),
         "Make": request.args.get('Make'),
         "Model": request.args.get('Model'),
         "result": predict_proba('Year','Mileage','State','Make','Model')
        }, 200
    


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8889)