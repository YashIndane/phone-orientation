# phone-orientation
A webapp that displays is your phone upright or up-side down

# Working

Sensorstream app continously sends the sensor values to [up-down-API.py](https://github.com/YashIndane/phone-orientation/blob/main/cgi-bin/up-down-API.py). The JS file in the flask app [home.js](https://github.com/YashIndane/phone-orientation/blob/main/static/home.js) continously sends `GET` request to the [up-down-API.py](https://github.com/YashIndane/phone-orientation/blob/main/cgi-bin/up-down-API.py) and with the help of `cgi` Python module the orientation of the phone is send as a response. According to the response [home.js](https://github.com/YashIndane/phone-orientation/blob/main/static/home.js) adjusts the image on browser.

![](https://github.com/YashIndane/repo-images/blob/main/phoneorien.png)

# Installations

## If directly using the Webapp without training own model

Keras

```
pip install keras
```

Tensorflow

```
pip install tensorflow
```
