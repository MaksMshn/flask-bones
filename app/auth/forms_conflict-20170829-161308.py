from flask_wtf import Form
from flask_babel import gettext
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

from app.user.models import User


class LoginForm(Form):
    email = TextField(gettext('Email'), validators=[DataRequired()])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        self.user = User.query.filter_by(email=self.email.data).first()

        if not self.user:
            self.email.errors.append(gettext('Unknown email'))
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append(gettext('Invalid password'))
            return False

        if not self.user.active:
            self.email.errors.append(gettext('User not activated'))
            return False

        return True
