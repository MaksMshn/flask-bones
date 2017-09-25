from flask_wtf import FlaskForm
from flask_babel import gettext as _
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.user.models import User


class UserForm(FlaskForm):
    email = StringField(
        _('Email'), validators=[Email(),
                                      DataRequired(),
                                      Length(max=128)])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)


class RegisterUserForm(UserForm):
    password = PasswordField(
        _('Password'),
        validators=[
            DataRequired(),
            EqualTo(
                'confirm',
                message=_('Passwords must match')
            ),
            Length(min=6, max=100)
        ]
    )
    confirm = PasswordField(
        _('Confirm Password'), validators=[DataRequired()]
    )
    accept_tos = BooleanField(
        _('I accept the TOS'), validators=[DataRequired()]
    )

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append(_('Email already registered'))
            return False

        self.user = user
        return True


class EditUserForm(UserForm):
    is_admin = BooleanField(_('Admin'))
    active = BooleanField(_('Activated'))
