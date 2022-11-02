import re


class Morph:
    def __init__(self, *args):
        self.words_lst = list(map(lambda x: x.strip(' .,!?:;').lower(), args))

    def __eq__(self, word):
        return word.lower() in self.words_lst

    def add_word(self, word):
        if word.lower() in self.words_lst:
            return
        self.words_lst.append(word.lower())

    def get_words(self):
        return tuple(self.words_lst)


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

text = ''.join(re.findall(r'[ а-я]', input().lower())).split()
res = sum(word == morph for word in text for morph in dict_words)
print(res)