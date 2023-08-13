from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services.special import get_string_homework

app = Flask(__name__)


@app.route("/")
@app.route("/start")
@app.route("/start/")
def start():
    return get_string_homework()


@app.route("/Привет мир")
def hello_word():
    return "<h4> Hello world!</h4>"


@app.route("/Привет мир/<string:name>/<int:number>")
def hello_word_with_name_and_number(name, number):
    return f"<h4> Hello {name}! Your number is {number}. </h4>"


@app.route("/Привет мир/")
@use_args({"name": fields.Str(reuired=True), "number": fields.Str(required=True)}, location="query")
def hello_word_with_name_and_number_args(args):
    name = args["name"]
    number = args["number"]
    return f"<h4> Hello {name}! Your number is {number}. </h4>"
