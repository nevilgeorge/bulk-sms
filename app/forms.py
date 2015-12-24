# forms.py
from app import db, models
from flask.ext.wtf import Form
from wtforms import FileField, SelectMultipleField, StringField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired

class SendMessageForm(Form):

    """Form used to send a message to a subscription."""

    message_text = TextAreaField('message_text', validators=[DataRequired()])
    subs = ['Hackers', 'Mentors', 'Judges']
    subscriptions = SelectMultipleField(
        'subscriptions',
        choices=[(s.lower(), s) for s in subs],
        validators=[DataRequired()]
    )


class AddNumberForm(Form):

    """Form used to add a new to/from number."""

    number = StringField('Number', validators=[DataRequired()])

    subscriptions = models.Subscription.query.all()
    choices = [(str(sub.id), sub.title) for sub in subscriptions]
    subscription = SelectField('Subscription', choices=choices, validators=[DataRequired()])


class AddSenderForm(Form):

    """Form used to add a new to/from number."""

    sender_number = StringField('from_number', validators=[DataRequired()])


class UploadFileForm(Form):

    """Form used to upload a csv/txt file of numbers."""

    number_file = FileField('Number File', validators=[DataRequired()])

    subscriptions = models.Subscription.query.all()
    choices = [(str(sub.id), sub.title) for sub in subscriptions]
    subscription = SelectField('Subscription', choices=choices, validators=[DataRequired()])


class AddSubscriptionForm(Form):

    """Form used to create a new subscription."""

    title = StringField('name', validators=[DataRequired()])
