import json
import unittest
from flask import Flask
from pprint import pprint
from app import app, datetime

app.config.from_object('config.DevelopmentConfig')

from app.views import *
from dbDriver import db

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """ This is the requests test predifined values """

        self.client = app.test_client()

        db.create_tables()

    def tearDown(self):
        db.drop_tables()

    def register_user(self, username, email, password):
        """ use to register a demo user """

        return self.client.post(
        '/api/v1/auth/signup', data=json.dumps(dict(username=username, email=email, password=password)), content_type='application/json')
