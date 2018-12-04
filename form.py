from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange, Length


class AddPetForm(FlaskForm):
    """form for adding pets"""
    name = StringField(
        "Pet Name", validators=[InputRequired(),
                                Length(min=0, max=50)])
    species = StringField(
        "Species Name",
        validators=[
            InputRequired(),
            AnyOf(values=['cat', 'dog', 'porcupine'])
        ])
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    age = IntegerField(
        "Pet Age", validators=[InputRequired(),
                               NumberRange(min=0, max=30)])
    notes = TextAreaField(
        "Pet Notes", validators=[Optional(),
                                 Length(min=0, max=300)])


class PetForm(FlaskForm):
    """form to display pet info and edit"""
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    notes = TextAreaField("Pet Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])
