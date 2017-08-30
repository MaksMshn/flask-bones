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


# Db commands
@cli.command()
def initdb():
    """Initialize the database."""
    db.create_all()


@cli.command()
def dropdb():
    """Drop the database."""
    db.drop_all()


# Start script
cli.add_command(MigrateCommand, "db")


if __name__ == '__main__':
    cli()
