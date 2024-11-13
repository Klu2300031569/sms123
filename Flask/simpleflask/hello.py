from flask import Flask             # import flask
klu = Flask(__name__)               # create an app instance
@klu.route("/")                     # at the end point /
def hello():                        # call method hello
    return "Hello World!"

@klu.route("/S32")
def hello1():
    return "<h1><font color ='blue'><center>Now am in S32 Section</center></font><h1>"
      # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    klu.run()