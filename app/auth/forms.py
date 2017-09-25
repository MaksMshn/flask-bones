from flask_wtf import FlaskForm
from flask_babel import gettext as _
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app.user.models import User


class LoginForm(FlaskForm):
    email = StringField(_('Email'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        self.user = User.query.filter_by(email=self.email.data).first()

        if not self.user:
            self.email.errors.append(_('Unknown email'))
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append(_('Invalid password'))
            return False

        if not self.user.active:
            self.email.errors.append(_('User not activated'))
            return False

        return True
