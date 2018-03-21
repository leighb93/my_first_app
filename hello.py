from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
		return "Hello Leigh!"


@app.route("/idontexist")
def idontexist():
		return "I do exist now!"

app.run(debug=True)