from flask import Flask, render_template

app = Flask("Phone_orientation_app")

@app.route("/home")
def display_page():
    return render_template("index.html")

app.run(host="0.0.0.0", port=48)