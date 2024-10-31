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

    # ========= US 4 =========

    def test_single_word_starting_with_consonant_or_y_moves_first_letter_to_end_and_appends_ay(self):
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    # ========= US 5 =========

    def test_single_word_starting_with_more_consonants_moves_consonants_to_end_and_appends_ay(self):
        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_single_word_starting_with_four_consonants_moves_consonants_to_end_and_appends_ay(self):
        translator = PigLatin("chthonic")
        self.assertEqual("onicchthay", translator.translate())

