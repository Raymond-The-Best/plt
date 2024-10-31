import unittest

from transformers.tools.evaluate_agent import translator

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    # ========= US 1 =========

    def test_create_translator(self):
        translator = PigLatin("hello world")
        self.assertTrue(isinstance(translator, PigLatin))

    def test_create_translator_and_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    # ========= US 2 =========

    def test_create_translator_empty_phrase(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    # ========= US 3 =========

    def test_single_word_starting_with_vowel_ending_in_y_appends_nay(self):
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_single_word_starting_with_vowel_ending_with_vowel_appends_yay(self):
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_single_word_starting_with_vowel_ending_with_consonant_appends_ay(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())