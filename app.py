from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello World</h1>"

@app.route("/username/<username>")
def username_fetch(username):
    return username

@app.route("/posts/<int:post_id>")
def get_id(post_id):
    return post_id

@app.route("/dashboard", methods = ['GET', 'POST'])
def user_dash():
    if request.method == 'GET':
        return "load the page"
    else:
        return "Upload your data here"