import unittest
import requests_mock
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPage(TestBase):
    def test_human_ranger(self):
        mock.get("http://classapi:5000/class", text="ranger")
        mock.get("http://raceapi:5000/race", text="Human")
        mock.post("http://nameapi:5000/name", text="Stor")
        mock.post("http://nameapi:5000/name", text="Hornraven")
        response = self.client.get(url_for("character"))
        self.assertIn(b"Your Race is Human", response.data)