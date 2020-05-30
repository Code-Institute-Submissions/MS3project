from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, optional


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    submit = SubmitField('Lets Go!')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    drink_name = StringField('Smoothie Name',
                              validators=[DataRequired()])
    description = TextAreaField('Smoothie Description',
                                       validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients',
                                       validators=[DataRequired()])
    directions = TextAreaField('Directions',
                                       validators=[DataRequired()])
    serves = IntegerField('Number of Servings', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time (mins)',
                                validators=[DataRequired()])
    img_url = StringField('Smoothie Image', validators=[DataRequired()])
    category_name = IntegerField('Smoothie category',
                                validators=[DataRequired()])
    submit = SubmitField('Add Recipe')