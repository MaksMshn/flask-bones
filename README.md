flask-bones
===========


## Setup

0. Setup environment 

    Using vagrant:

    ```
    $ git clone https://github.com/MaksMshn/flask-bones
    $ cd flask-bones
    $ vagrant up
    $ vagrant ssh
    $ cd /vagrant
    ```

    Or by simply installing anaconda and yarn.


1. Install Python packages:

    ```
    $ make init
    $ source activate flask-bones
    ```

2. Overwrite default parameters in config/flask_config.py

    ```
    SITE_NAME = 'My site name'
    SECRET_KEY = 'use os.urandom(20) to produce sth very random'
    SQLALCHEMY_DATABASE_URI = 'postgresql://USER:PASSWORD@localhost:5432/DBNAME'
    # if you dont want to use dedicate email server you can
    # simply use an existing gmail account by setting
    MAIL_USERNAME = 'YOUR_GMAIL_ACCOUNT@gmail.com'
    MAIL_PASSWORD = 'YOUR_GMAIL_PASSWORD'
    ```

4. Install Javascript dependencies:

    ```
    $ make assets
    ```

5. Setup database and create admin

    ```
    $ make db
    $ make admin
    ```
6. Test your setup

    ```
    $ make test
    ```


7. Run devserver 

    ```
    $ make devserver
    ```

8. Check that the site is working

    Head to http://localhost:5000 and login using admin account set up earlier.


## Run production server

Use nginx to serve static file and uwsgi as a container.

    ```
    $ sudo cp config/app /etc/nginx/sites-enabled
    $ sudo rm /etc/nginx/sites-enabled/default
    $ sudo service nginx restart
    $ uwsgi --socket 0.0.0.0:5000 --protocol=http -w run_server
    ```
    

## Features

1. Version your database schema

    ```bash
    # Display the current revision
    $ python manage.py db current
    1fb7c6da302 (head)

    # Create a new migration
    $ python manage.py db revision

    # Upgrade the database to a later version
    $ python manage.py db upgrade
    ```

2. Internationalize the application for other languages (i18n)

    ```bash
    # Extract strings from source and compile a catalog (.pot)
    $ pybabel extract -F babel.cfg -o i18n/messages.pot .

    # Create a new resource (.po) for German translators
    $ pybabel init -i i81n/messages.pot -d i18n -l de

    # Compile translations (.mo)
    $ pybabel compile -d i18n

    # Merge changes into resource files
    $ pybabel update -i i18n/messages.pot -d i18n
    ```

