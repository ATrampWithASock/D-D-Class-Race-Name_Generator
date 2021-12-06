import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFirstname(TestBase):
    def test_human(self):
        response = self.client.post(url_for("firstname"), data="Human")
        self.assertIn(b'Stor', response.data)

    def test_dwarf(self):
        response = self.client.post(url_for("firstname"), data="Dwarf")
        self.assertIn(b'Dagney', response.data)

    def test_elf(self):
        response = self.client.post(url_for("firstname"), data="Elf")
        self.assertIn(b'Sharos', response.data)

    def test_orc(self):
        response = self.client.post(url_for("firstname"), data="Orc")
        self.assertIn(b'Turrf', response.data)

    def test_halfelf(self):
        response = self.client.post(url_for("firstname"), data="Half-Elf")
        self.assertIn(b'Faeryl', response.data)

    def test_dragonborn(self):
        response = self.client.post(url_for("firstname"), data="Dragonborn")
        self.assertIn(b'Killinaar', response.data)

class TestSurname(TestBase):
    def test_ranger(self):
        response = self.client.post(url_for("surname"), data="ranger")
        self.assertIn(b'Hornraven', response.data)

    def test_fighter(self):
        response = self.client.post(url_for("surname"), data="fighter")
        self.assertIn(b'Axebreaker', response.data)

    def test_wizard(self):
        response = self.client.post(url_for("surname"), data="wizard")
        self.assertIn(b'Arcanos', response.data)

    def test_druid(self):
        response = self.client.post(url_for("surname"), data="druid")
        self.assertIn(b'Hallowhawk', response.data)

    def test_barbarian(self):
        response = self.client.post(url_for("surname"), data="barbarian")
        self.assertIn(b'Shieldshatterer', response.data)

    def test_warlock(self):
        response = self.client.post(url_for("surname"), data="warlock")
        self.assertIn(b'Darkspawn', response.data)