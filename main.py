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

code = {'A':f'▄\u00A0▄▄▄',
        'B':'▄▄▄\u00A0▄\u00A0▄\u00A0▄',
	    'C':'▄▄▄\u00A0▄\u00A0▄▄▄\u00A0▄',
	    'D':'▄▄▄\u00A0▄\u00A0▄',
	    'E':'▄',
	    'F':'▄\u00A0▄\u00A0▄▄▄\u00A0▄',
	    'G':'▄▄▄\u00A0▄▄▄\u00A0▄',
	    'H':'▄\u00A0▄\u00A0▄\u00A0▄',
	    'I':'▄\u00A0▄',
	    'J':'▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄',
	    'K':'▄▄▄\u00A0▄\u00A0▄▄▄',
	    'L':'▄\u00A0▄▄▄\u00A0▄\u00A0▄',
	    'M':'▄▄▄\u00A0▄▄▄',
	    'N':'▄▄▄\u00A0▄',
	    'O':'▄▄▄\u00A0▄▄▄\u00A0▄▄▄',
	    'P':'▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄',
	    'Q':'▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄▄▄',
	    'R':'▄\u00A0▄▄▄\u00A0▄',
	    'S':'▄\u00A0▄\u00A0▄',
	    'T':'▄▄▄',
	    'U':'▄\u00A0▄\u00A0▄▄▄',
	    'V':'▄\u00A0▄\u00A0▄\u00A0▄▄▄',
	    'W':'▄\u00A0▄▄▄\u00A0▄▄▄',
	    'X':'▄▄▄\u00A0▄\u00A0▄\u00A0▄▄▄',
	    'Y':'▄▄▄\u00A0▄\u00A0▄▄▄\u00A0▄▄▄',
	    'Z':'▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄',
	    '0':'▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄',
	    '1':'▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄',
	    '2':'▄\u00A0▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄',
	    '3':'▄\u00A0▄\u00A0▄\u00A0▄▄▄\u00A0▄▄▄',
	    '4':'▄\u00A0▄\u00A0▄\u00A0▄\u00A0▄▄▄',
	    '5':'▄\u00A0▄\u00A0▄\u00A0▄\u00A0▄',
	    '6':'▄▄▄\u00A0▄\u00A0▄\u00A0▄\u00A0▄',
	    '7':'▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄\u00A0▄',
	    '8':'▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄',
	    '9':'▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄',
        ".":'▄\u00A0▄▄▄\u00A0▄\u00A0▄▄▄\u00A0▄\u00A0▄▄▄',
        ",":'▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄\u00A0▄▄▄\u00A0▄▄▄',
        "?":'▄\u00A0▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄\u00A0▄',
        "'":'▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄▄▄\u00A0▄',
        " ":'    '} #word space is 7 - we will add 3 more below so just add 4 here

class BasicForm(FlaskForm):
	user_input = StringField("Text to encode", validators=[DataRequired()])
	submit = SubmitField("Encode")

def encode(to_encode):
	# to_encode = input("Enter a phrase to encode:")
	converted = "   " #every word will end with 4 spaces which mean each line starts with 3 spaces
	for char in to_encode:
		converted += code[char.upper()] + '\u00A0\u00A0\u00A0' #3 spaces to denote a letter space
	print(converted)
	return converted

if __name__ == "__main__":
	app.run(debug=True)
