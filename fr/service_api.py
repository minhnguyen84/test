import os
import unittest
from unittest.mock import Mock

class MotsInterditsServices:
    def __init__(self, api_mots_interdit):
        self.api_mots_interdit = api_mots_interdit

    def find_text(self, text):
        text_split = text.lower().split(" ")
        mots_interdit_list = set(text_split).intersection(self.api_mots_interdit.get_mots_interdit())
        return mots_interdit_list


class MotsInterditsApiServicesTest(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()
        self.mock.get_mots_interdit.return_value = ["toto", "tata"]
        self.mots_interdits_service = MotsInterditsServices(self.mock)

    def test_ne_contient_pas_de_mot_interdit(self):
        self.assertEqual(self.mots_interdits_service.find_text("bonjour Marc"), set())

    def test_contient_aumoins_1mot_interdit(self):
        self.assertEqual(self.mots_interdits_service.find_text("bonjour belle petite fille blabla toto"), {'toto'})

    def test_contient_aumoins_1mot_interdit_majuscule(self):
        # re-define api
        self.mock.get_mots_interdit.return_value = ["coca", "bouger", "fille", "belle"]
        self.assertEqual(self.mots_interdits_service.find_text("bonjour belle petite FILLE"), {'fille', 'belle'})


if __name__ == '__main__':
    unittest.main()
