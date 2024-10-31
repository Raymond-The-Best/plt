
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
                else:
                    translated_words.append(word + 'yay')
            else:
                # Placeholder for other translation rules
                translated_words.append(word)
        return ' '.join(translated_words)

