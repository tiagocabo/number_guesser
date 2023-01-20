import tensorflow as tf
import datetime


mnist = tf.keras.datasets.mnist

# 28x28 pixel image
(x_train, y_train),(x_test, y_test) = mnist.load_data()

# normalize vector
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# converts RGB values to binary 0 = white, 1 black
for train in range(len(x_train)):
    for row in range(28):
        for x in range(28):
            if x_train[train][row][x] != 0:
                x_train[train][row][x] = 1

# linear set of layers
model = tf.keras.models.Sequential()
# need to convert matrix input to a linear vector
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

print('start fit')
model.fit(x=x_train,
          y=y_train,
          epochs=150,
          validation_data=(x_test, y_test),
          callbacks=[tensorboard_callback])
model.save('epic_num_reader_v2.model')

print("Model saved")