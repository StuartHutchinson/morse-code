import os

from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["FLASK_KEY"]
bootstrap = Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def index():
	# return "Test"
	form = BasicForm()
	encoded = ""
	if form.validate_on_submit():
		encoded = encode(form.user_input.data)
	return render_template("index.html", form=form, encoded=encoded)

code = {'A':'▄ ▄▄▄',
        'B':'▄▄▄ ▄ ▄ ▄',
	    'C':'▄▄▄ ▄ ▄▄▄ ▄',
	    'D':'▄▄▄ ▄ ▄',
	    'E':'▄',
	    'F':'▄ ▄ ▄▄▄ ▄',
	    'G':'▄▄▄ ▄▄▄ ▄',
	    'H':'▄ ▄ ▄ ▄',
	    'I':'▄ ▄',
	    'J':'▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    'K':'▄▄▄ ▄ ▄▄▄',
	    'L':'▄ ▄▄▄ ▄ ▄',
	    'M':'▄▄▄ ▄▄▄',
	    'N':'▄▄▄ ▄',
	    'O':'▄▄▄ ▄▄▄ ▄▄▄',
	    'P':'▄ ▄▄▄ ▄▄▄ ▄',
	    'Q':'▄▄▄ ▄▄▄ ▄ ▄▄▄',
	    'R':'▄ ▄▄▄ ▄',
	    'S':'▄ ▄ ▄',
	    'T':'▄▄▄',
	    'U':'▄ ▄ ▄▄▄',
	    'V':'▄ ▄ ▄ ▄▄▄',
	    'W':'▄ ▄▄▄ ▄▄▄',
	    'X':'▄▄▄ ▄ ▄ ▄▄▄',
	    'Y':'▄▄▄ ▄ ▄▄▄ ▄▄▄',
	    'Z':'▄▄▄ ▄▄▄ ▄ ▄',
	    '0':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '1':'▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '2':'▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄',
	    '3':'▄ ▄ ▄ ▄▄▄ ▄▄▄',
	    '4':'▄ ▄ ▄ ▄ ▄▄▄',
	    '5':'▄ ▄ ▄ ▄ ▄',
	    '6':'▄▄▄ ▄ ▄ ▄ ▄',
	    '7':'▄▄▄ ▄▄▄ ▄ ▄ ▄',
	    '8':'▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄',
	    '9':'▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
        ".":'▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄',
        ",":'▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄',
        "?":'▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄',
        "'":'▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
        " ":'    '} #word space is 7 - we will add 3 more below so just add 4 here

class BasicForm(FlaskForm):
	user_input = StringField("Text to encode", validators=[DataRequired()])
	submit = SubmitField("Encode")

def encode(to_encode):
	# to_encode = input("Enter a phrase to encode:")
	converted = ""
	for char in to_encode:
		converted += code[char.upper()] + '   ' #3 spaces to denote a letter space
	print(converted)
	return converted

if __name__ == "__main__":
	app.run(debug=True)
