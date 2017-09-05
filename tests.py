from app import create_app
from app.config import test_config
from app.database import db, populate_db
from app.user.models import User
from sqlalchemy.sql.expression import func
from faker import Factory
import unittest

admin_email = 'cburmeister@discogs.com'
admin_password = 'test123'

fake = Factory.create()


print("Using: {} database\n\n\n".format(test_config.SQLALCHEMY_DATABASE_URI))


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run once at the start"""
        app = create_app(test_config)
        db.app = app  # hack for using db.init_app(app) in app/__init__.py
        db.drop_all()
        db.create_all()
        populate_db()
        cls.app = app

    @classmethod
    def tearDownClass(cls):
        """ Run after all tests. """
        db.drop_all()

    def setUp(self):
        """ Run before each test """
        self.app = self.app.test_client()

    def tearDown(self):
        """ Run after each test """
        # in case we had an error somewhere
        db.session.rollback()

    def get_non_admin_user(self):
        return User.query.filter_by(
            is_admin=False).order_by(func.random()).first()

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def register_user(self, email, password):
        return self.app.post('/register', data=dict(
            email=email,
            password=password,
            confirm=password,
            accept_tos=True
        ), follow_redirects=True)

    def edit_user(self, user, email):
        return self.app.post('/user/edit/%s' % user.id, data=dict(
            email=user.email,
        ), follow_redirects=True)

    def delete_user(self, uid):
        return self.app.get('/user/delete/%s' % uid, follow_redirects=True)

    def test_404(self):
        print()
        resp = self.app.get('/nope', follow_redirects=True)
        assert 'Page Not Found' in resp.data.decode("utf8")

    def test_index(self):
        resp = self.app.get('/index', follow_redirects=True)
        assert 'Flask Bones' in resp.data.decode("utf8")

    def test_login(self):
        resp = self.login(admin_email, admin_password)
        assert 'You were logged in' in resp.data.decode("utf8")

    def test_logout(self):
        resp = self.login(admin_email, admin_password)
        resp = self.app.get('/logout', follow_redirects=True)
        assert 'You were logged out' in resp.data.decode("utf8")

    def test_register_user(self):
        email = fake.email()
        password = fake.word() + fake.word()
        resp = self.register_user(email, password)
        assert 'Sent verification email to %s' % email in resp.data.decode(
            "utf8")

    def test_edit_user(self):
        user = self.get_non_admin_user()
        resp = self.login(admin_email, admin_password)
        resp = self.edit_user(user, email=fake.email())
        assert 'User %s edited' % user.email in resp.data.decode("utf8")

    def test_delete_user(self):
        user = self.get_non_admin_user()
        resp = self.login(admin_email, admin_password)
        resp = self.delete_user(user.id)
        assert 'User %s deleted' % user.email in resp.data.decode("utf8")

    def test_user_list(self):
        resp = self.login(admin_email, admin_password)
        resp = self.app.get('/user/list', follow_redirects=True)
        assert 'Users' in resp.data.decode("utf8")


if __name__ == '__main__':
    unittest.main(verbosity=2)
