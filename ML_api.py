
from flask import Flask, request
from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS


from flasgger import Swagger
import pandas as pd
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)


swagger = Swagger(app)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Generates documentation for iris predictor
    ---
    parameters:
      - name: id
        in: formData
        type: number
        required: true
    """
    # render_template('index.html', prediction=3)
    return "3"


if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)