# Guessing the numbers using AI

This project was based on the https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg video were he used a pygame interface to draw a number and predicting the number using the mnist dataset to train. 

I trained his DNN model and made a CNN version. 
This is the current version. 
![ezgif.com-video-to-gif (1)](./images/guess_number.gif)

I follow the training using tensorboard. Check below the results. 
![model_training](/images/model_training.png)

# Getting started

To setup this project in your laptop, please clone the repo em make

```bash
make venv
```

Then init the project and test a couple predictions,
```python
source venv/bin/activate

python draw_number.py
```


