import os
import unittest
from unittest.mock import MagicMock, Mock

from fr.api import api_mots_interdit

names = ["coca", "bouger", "fille", "belle"]


def find_text(text):
    text_split = text.lower().split(" ")
    mots_interdit_list = set(text_split).intersection(names)
    return mots_interdit_list


class MotsInterditsSimpleServicesTest(unittest.TestCase):

    def test_ne_contient_pas_de_mot_interdit(self):
        self.assertEqual(find_text("bonjour Marc"), set())

    def test_contient_aumoins_1mot_interdit(self):
        self.assertEqual(find_text("bonjour belle petite fille blabla toto"), {'fille', 'belle'})

    def test_contient_aumoins_1mot_interdit_majuscule(self):
        self.assertEqual(find_text("bonjour belle petite FILLE"), {'fille', 'belle'})


if __name__ == '__main__':
    unittest.main()
