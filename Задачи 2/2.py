class Paragraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = self.words[0]
        result = ''
        align_method = self._get_align_method()

        for i in range(1, len(self.words) + 1):
            if i == len(self.words) and ' ' in line:
                result += align_method(line, self.width)
                break
            if len(line + self.words[i] + ' ') > self.width:
                result += align_method(line, self.width) + '\n'
                line = self.words[i]
            else:
                line += ' ' + self.words[i]
        
        print(result)


class LeftParagraph(Paragraph):
    def _get_align_method(self):
        return str.ljust


class RightParagraph(Paragraph):
    def _get_align_method(self):
        return str.rjust

# Пример использования
lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()