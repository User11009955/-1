class MinMaxWordFinder:
    def __init__(self) -> None:
        self.sentence = ''

    def add_sentence(self, sentence):
        self.sentence += ' ' + ' '.join([i for i in sentence.split()])
        print(self.sentence)
    
    def shortest_words(self):
        words = sorted(self.sentence.split(), key=len)
        shortest_length = len(words[0])
        shortest_words = [word for word in words if len(word) == shortest_length]
        return sorted(shortest_words)
            
    def longest_words(self):
        words = sorted(set(self.sentence.split()), key=len, reverse=True)
        longest_length = len(words[0])
        longest_words = [word for word in words if len(word) == longest_length]
        return sorted(longest_words)