#!/user/bin/env python
from setuptools import setup

setup(name = 'graffiti-backend',
      version = '3.0',
      description = 'Graffiti backend based on Django framework.',
      author = 'Zhong Yang',
      author_email = 'yzhnasa@gmail.com',
      url = 'https://bitbucket.org/dreamer2018/graffiti_backend_v3.0.git',
      install_requires=[
        'django>=2.0.1',
        'django-filter>=1.1.0',
        'django-jwt-auth>=0.0.2',
        'djangorestframework>=3.7.7',
        'djangorestframework-gis>=0.12',
        'djangorestframework-jwt>=1.11.0',
        'django-celery>=3.1.17',
        'graphene>=2.0.1',
        'graphene-django>=2.0.0',
        'graphql-core>=2.0',
        'graphql-relay>=0.4.5',
        #'pdb>=0.1',
        'Pillow>=5.0.0',
        'postgis>=1.0.4',
        'postgres>=2.2.1',
        'psycopg2>=2.7.3.2',
        'PyJWT>=1.5.3',
        'requests>=2.18.4',
        'cryptography>=2.1.4',
        'python-jose>=2.0.0',
        #'enum>=1.1.6',
        'rest-framework-auth0>=0.4.6',
        'psycopg2>=2.6.1',
        'mod-wsgi>=4.5.24',
        'mod-wsgi-httpd>=2.4.27.1'
      ]
)
