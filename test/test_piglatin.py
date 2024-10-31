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
        self.assertEqual(translator.get_phrase(), "hello world")

    # ========= US 2 =========

    def test_create_translator_empty_phrase(self):
        translator = PigLatin("")
        self.assertEqual(translator.translate(), "nil")

    # ========= US 3 =========

    def test_single_word_starting_with_vowel_ending_in_y_appends_nay(self):
        translator = PigLatin("any")
        self.assertEqual(translator.translate(), "anynay")