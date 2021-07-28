#!/usr/bin/python
from flask import Flask, request
from model_deployment_VF import predict_price

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def Pricepredict():
    return {
         "Precio Estimado": predict_price(request.args.get('YEAR'), request.args.get('MILEAGE'),request.args.get('STATE'), request.args.get('MAKE'), request.args.get('MODEL'))
        }, 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)