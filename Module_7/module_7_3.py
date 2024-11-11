class WordsFinder:
    delete_symbols: list = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_name):
        self.file_name: tuple = file_name

    def get_all_words(self) -> dict:
        all_words = {}
        for name in self.file_name:
            words = []
            with open(name, encoding='utf-8') as file:
                text = ''
                for line in file:
                    text += line.lower()
                    for symbol in self.delete_symbols:
                        if symbol in text:
                            text = text.replace(symbol, '')
                words = text.split()
            all_words[name] = words
        return all_words

    def find(self, word: str) -> dict:
        word_position = {}
        for name, word_list in self.get_all_words().items():
            num = 0
            if word.lower() in word_list:
                for i in range(len(word_list)):
                    if word.lower() == word_list[i]:
                        num = i + 1
                        break
            word_position[name] = num
        return word_position

    def count(self, word: str) -> dict:
        word_count = {}
        for name, word_list in self.get_all_words().items():
            count_num = 0
            if word.lower() in word_list:
                for i in range(len(word_list)):
                    if word.lower() == word_list[i]:
                        count_num += 1
            word_count[name] = count_num
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего