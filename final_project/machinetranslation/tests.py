import unittest

from translator import english_to_french, french_to_english

class TestEnToFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hi"), "Bonjour")
    def test2(self):
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

    

class TestFrToEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test2(self):
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")


unittest.main()