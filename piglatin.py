
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
            if word[0] in 'aeiou':
                if word[-1] == 'y':
                    translated_words.append(word + 'nay')
                elif word[-1] in 'aeiou':
                    translated_words.append(word + 'yay')
                else:
                    translated_words.append(word + 'ay')
            else:
                # Handling words starting with a consonant or 'y'
                translated_words.append(word[1:] + word[0] + 'ay')
        return ' '.join(translated_words)

