#Graffiti-Backend_v3.0

##Make a fork and clone to your local

    $ git clone https://<your_name>@bitbucket.org/dreamer2018/graffiti_backend_v3.0.git

##Install pip
###Red hat
    $ sudo easy_install pip

##postgreSQL

###Mac Os

####Install homebrew

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

####Install postgreSQL

    $ brew install postgres
    $ brew install postgresql
    $ brew install postgis
    $ brew install gdal
    $ brew install libgeoip

####Start postgres at login

    $ mkdir -p ~/Library/LaunchAgents
    $ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
    $ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

####Connecting to default database

    $ psql postgres

####Install postgreSQL

    $ sudo apt-get install postgresql postgresql-contrib

####Initialize postgres

    $ initdb /usr/local/var/postgres
    $ sudo -u postgres psql postgres
####Connecting to default database

    $ sudo -u postgres -i

###Create database

    postgres=# CREATE DATABASE graffiti_db;
So now you can connect to graffiti database.

    $ psql graffiti_db

###Create role as superuser with password

    graffiti_db=# CREATE USER graffiti_manager WITH SUPERUSER PASSWORD 'graffiti';

##Setup virtual environment

Install virtualenv

    $ sudo pip install virtualenv

Create virtual environment

    $ virtualenv env

Activate virtual environment

    $ source env/bin/activate

Deactivate virtual environment

    $ deactivate                             // Turn off virtual enviroment when we don't need it.

##Install Django and Django plugins(assume virtual environment activated)

###Install with pip

Install setuptools

    $ pip3 install setuptools

Install plugins

    $ pip3 install -e .

###Manual install

Install Django framework

    $ pip3 install django;

Install Django restful framework

    $ pip3 install djangorestframework        // Support REST style API and JSON format.

Install Django restful GIS framework

    $ pip3 install djangorestframework-gis    // Support GeoJSON format.

Install Django-celery

    $ pip3 install django-celery              // Server side schedualed task.

##If database migrate fail, please try those instructions

Reinstall postgis(iOS)

    $ brew reinstall postgis -s
    $ pip3 install -e .

CentOS, Amazon Linux

    $ sudo pip-3.6 install psycopg2
    $ sudo yum install libjpeg-devel
    $ sudo yum install freetype-devel
    $ sudo yum install libpng-devel
    $ sudo pip install Pillow

Reinstall sfcgal

    $ brew install cmake
    $ brew reinstall sfcgal --build-from-source

Install Postgres+PostGIS on Amazon Linux

    $ http://codingsteps.com/installing-and-configuring-postgresql-in-amazon-linux-ami/

##Testing Tool
    $ brew install httpie

##Run server locally
    $ python3 manage.py makemigrations <app_name>    # eg. python3 manage.py makemigraions user_authentication
    $ python3 manage.py migrate
    $ python3 manage.py runserver

##Deploy

###Install httpd and mod_wsgi

    $ pip install mod_wsgi-httpd

Download mod_wsgi and then

    $ tar -xvf *.tar
    $ cd mod*
    $ sudo yum install httpd-devel
    $ sudo python setup.py install

###Start database
    $ sudo service postgresql96 initdb
    $ sudo service postgresql96 start

###httpd server commands

    $ service httpd start
    $ service httpd restart
    $ service httpd stop

###Postgis Install
    https://gist.github.com/whyvez/8d19096712ea44ba66b0