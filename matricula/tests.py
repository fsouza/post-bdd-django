"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.failUnlessEqual(1 + 1, 2)

    def test_deve_efetuar_uma_soma_de_1_com_1(self):
        self.failUnlessEqual(1 + 1, 2)

