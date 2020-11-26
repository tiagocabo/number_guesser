
from flask import Flask, request
from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
import tensorflow as tf

from flasgger import Swagger
import pandas as pd
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

import matplotlib.pyplot as plt
import numpy as np


swagger = Swagger(app)


@app.route('/predict', methods=[ 'POST'])
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

    #DATA = request.args.get("pixels")
    DATA = request.form["pixels"]
    
    #path = request.files.get("input_file")
    #path = "/home/local/FARFETCH/tiago.cabo/Desktop/numbers.txt"

    #with open(path) as file:
    #  DATA = file.readlines()

    #data = data[0].split(',')

    #data = list(map(int, data))
    #data = data[0::4]
    #import numpy as np
    #matrix = np.array(data).reshape((28,28))

    #import matplotlib.pyplot as plt
    #plt.imshow(matrix,'Reds')
    #plt.show()
    DATA = DATA.split(',')
    print(DATA)
    DATA = list(map(int, DATA))
    DATA = DATA[0::4]
    matrix = np.array(DATA).reshape((28,28))

    model = tf.keras.models.load_model('CNN_v0.model')

    print(matrix)
    li = np.reshape(DATA, (1,28, 28, 1))
    predictions = model.predict(li)
    t = (np.argmax(predictions[0]))


    return str(t)


if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)