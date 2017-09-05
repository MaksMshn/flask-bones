import click
from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db


# Create and run app
def create_cli_app(info):
    from app.config import dev_config
    app = create_app(dev_config)
    Migrate(app, db)
    return app

@click.group(cls=FlaskGroup, create_app=create_cli_app)
def cli():
    pass


# # Db commands

@cli.command()
def initdb():
    """Initialize the database. The better way to do it is: "manage.py db upgrade head" """
    db.create_all()


@cli.command()
def dropdb():
    """Drop the database."""
    db.drop_all()


@cli.command()
@click.option('--email', prompt="Enter admin email.")
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def create_admin(email, password):
    """ Create site administrator. """
    from app.user import models
    app = create_app()
    with app.app_context():
        user = models.User.create(
        email=email,
        password=password,
        remote_addr="localhost",
        active=True,
        is_admin=True)

# Start script
cli.add_command(MigrateCommand, "db")


if __name__ == '__main__':
    cli()
