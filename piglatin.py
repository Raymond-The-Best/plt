
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        words = self.phrase.split()
        translated_words = []
        for word in words:
            if "-" in word:
                translated_subwords = []
                subwords = word.split("-")
                for subword in subwords:
                    translated_subwords.append(self.translate_single_word(subword))
                translated_words.append("-".join(translated_subwords))

            else:
                translated_words.append(self.translate_single_word(word))
        return ' '.join(translated_words)

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
            if len(word) > 1 and all(c not in 'aeiou' for c in word[:2]):
                # Move all leading consonants to the end
                index = 0
                while index < len(word) and word[index] not in 'aeiou':
                    index += 1
                translated_word = word[index:] + word[:index] + 'ay'
            else:
                translated_word = word[1:] + word[0] + 'ay'

        return translated_word
