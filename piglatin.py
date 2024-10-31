from error import PigLatinError

class PigLatin:
    AUTHED_PUNC = ".,;:'?!() -"

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if any(char in self.phrase for char in "[]{}"):
            raise PigLatinError()
        table = self.phrase.maketrans(PigLatin.AUTHED_PUNC, " "*len(PigLatin.AUTHED_PUNC))
        words = self.phrase.translate(table).split()
        translation_dict = {}
        for word in words:
            translation_dict[word] = {"isUppercase": word.isupper(),
                                      "isTitlecase": word[0].isupper(),
                                      "translation": self.translate_single_word(word.lower())}
        translated_phrase = self.phrase
        for word, translation in translation_dict.items():
            if translation["isUppercase"]:
                formatted_translation = translation["translation"].upper()
            elif translation["isTitlecase"]:
                formatted_translation = translation["translation"].title()
            else:
                formatted_translation = translation["translation"]
            translated_phrase = translated_phrase.replace(word, formatted_translation)

        return translated_phrase

    def translate_single_word(self, word: str) -> str:
        translated_word = ""
        if word[0] in 'aeiou':
            if word[-1] == 'y':
                translated_word = word + 'nay'
            elif word[-1] in 'aeiou':
                translated_word = word + 'yay'
            else:
                translated_word = word + 'ay'
        else:
            # Handling words starting with a consonant or 'y'
            index = 0
            while index < len(word) and word[index] not in 'aeiou':
                index += 1
            translated_word = word[index:] + word[:index] + 'ay'

        return translated_word