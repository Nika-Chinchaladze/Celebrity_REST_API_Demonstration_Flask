from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired

CATEGORY = [
    ("first_name", "first_name"),
    ("last_name", "last_name"),
    ("gender", "gender"),
    ("age", "age"),
    ("movie_genre", "movie_genre"),
    ("followers", "followers")
]
UPDATE_CATEGORY = [
    ("first_name", "first_name"),
    ("last_name", "last_name"),
    ("gender", "gender"),
    ("age", "age"),
    ("movie_genre", "movie_genre"),
    ("followers", "followers"),
    ("img_url", "img_url"),
]
OPERATORS = [("=", "="), (">", ">"), ("<", "<"), (">=", ">="), ("<=", "<=")]


class QuickForm(FlaskForm):
    category = SelectField("Choose Category", choices=CATEGORY, validators=[DataRequired()])
    operator = SelectField("Choose Operator - For Age or Followers Category - ONLY!",
                           choices=OPERATORS,
                           validators=[DataRequired()]
                           )
    valueField = StringField("Define Value", validators=[DataRequired()])
    submit = SubmitField("Search")


class AddForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    age = StringField("Age", validators=[DataRequired()])
    movie_genre = StringField("Movie Genre", validators=[DataRequired()])
    followers = StringField("Followers Quantity", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Celebrity")


class ChangeForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    age = StringField("Age", validators=[DataRequired()])
    movie_genre = StringField("Movie Genre", validators=[DataRequired()])
    followers = StringField("Followers Quantity", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Change Celebrity")


class UpdateForm(FlaskForm):
    category = SelectField("Choose Category", choices=UPDATE_CATEGORY, validators=[DataRequired()])
    valueField = StringField("Define Value", validators=[DataRequired()])
    submit = SubmitField("Update Celebrity")
