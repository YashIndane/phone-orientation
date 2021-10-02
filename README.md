![](https://img.shields.io/badge/-Python-grey?style=for-the-badge&logo=python) ![](https://img.shields.io/badge/-JS-grey?style=for-the-badge&logo=javascript) ![](https://img.shields.io/badge/-HTML-grey?style=for-the-badge&logo=html)

# phone-orientation
A webapp that displays is your phone upright or up-side down

Demo Link ->

## Working

Sensorstream app continously sends the sensor values to [up-down-API.py](https://github.com/YashIndane/phone-orientation/blob/main/cgi-bin/up-down-API.py). The JS file in the flask app [home.js](https://github.com/YashIndane/phone-orientation/blob/main/static/home.js) continously sends `GET` request to the [up-down-API.py](https://github.com/YashIndane/phone-orientation/blob/main/cgi-bin/up-down-API.py) and with the help of `cgi` Python module the orientation of the phone is send as a response. According to the response [home.js](https://github.com/YashIndane/phone-orientation/blob/main/static/home.js) adjusts the image on browser.

![](https://github.com/YashIndane/repo-images/blob/main/phoneorien.png)

## Installations

Keras

```
pip install keras
```

Tensorflow

```
pip install tensorflow
```

## App installation

Install Sensorstream IMU+GPS App from Google PlayStore.

![](https://github.com/YashIndane/repo-images/blob/main/imu.png)

## Training the model

If you need your own model then use [value_capture.py](https://github.com/YashIndane/phone-orientation/blob/main/value_capture.py) to first get the sensor data. Use Orientation sensor data for getting the orientation. Now use the [model_training.py](https://github.com/YashIndane/phone-orientation/blob/main/model_training.py) to train the model.
