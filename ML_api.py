import pickle
import sys

from flask import Flask, request
from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
import tensorflow as tf
from bson.binary import Binary
from flasgger import Swagger
import pandas as pd
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

import matplotlib.pyplot as plt
import numpy as np


swagger = Swagger(app)
model = tf.keras.models.load_model('CNN_v0.model')


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

    #import matplotlib.pyplot as plt
    #plt.imshow(matrix,'Reds')
    #plt.show()
    DATA = DATA.split(',')
    DATA = list(map(int, DATA))
    DATA = DATA[0::4]
    matrix = np.array(DATA).reshape(int(np.sqrt(len(DATA))),int(np.sqrt(len(DATA)))) 
    
    image = tf.constant(matrix)
    image = image[tf.newaxis, ..., tf.newaxis]
    
    resized_image = tf.image.resize(image, [28,28])



    resized_image = resized_image[0,...,0].numpy()
    from PIL import Image
    print(type(resized_image))
    print(resized_image)
    from matplotlib import pyplot as plt
    #plt.imshow(resized_image, interpolation='nearest')
    #plt.show()

    save_to_mongo = resized_image.tobytes()
    #save_to_mongo = "tiago"
    print(sys.getsizeof(save_to_mongo))
    print("save to mongo type:", type(save_to_mongo))
    
    resized_image = np.reshape(resized_image, (1,28, 28, 1))

    predictions = model.predict(resized_image)
    t = (np.argmax(predictions[0]))

    import pymongo

    mongo_secret = "dbUserPassword"
    db_name = "number_guesser"
    client = pymongo.MongoClient(
        f"mongodb+srv://dbUser:{mongo_secret}@cluster0.ymgtu.mongodb.net/{db_name}?retryWrites=true&w=majority")

    db = client.database

    result = {
        "draw_data": save_to_mongo,
        "prediction": int(t),
    }


    collection = db.number_guesser
    print("start to mongo")
    print(result)
    collection.insert_one(result)
    print("end write")
    return str(t)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)