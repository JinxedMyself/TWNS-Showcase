from flask_wtf import FlaskForm
from wtforms import StringField

class TweetForm(FlaskForm):
    author = StringField('Author', validators.length(max=100), default="Anon")
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')