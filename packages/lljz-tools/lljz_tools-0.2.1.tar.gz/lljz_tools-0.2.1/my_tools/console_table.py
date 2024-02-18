# coding=utf-8

from my_tools.log_manager import LogManager

logger = LogManager('ConsoleTable').get_logger()


class ConsoleTable:

    def __init__(self, data: list[dict]):  # noqa
        # assert data, 'data is empty!'
        self.rawData = data
        self._colWidth = 0
        self.header = list(data[0].keys()) if data else []
        self._header = []
        self._body = []
        self._stringWidth = {}

    def _getStrWidth(self, string):
        if string in self._stringWidth:
            return self._stringWidth[string]
        width = 0

        for s in string:
            if u'\u4e00' <= s <= u'\u9fff' or s in '【】（）—…￥！·、？。，《》：；‘“':
                width += 2
            else:
                width += 1
        self._stringWidth[string] = width
        self._colWidth = max(width, self._colWidth)
        return width

    @property
    def colWidth(self):
        if self._colWidth:
            return self._colWidth
        for h in self.header:
            self._getStrWidth(h)
        for row in self.rawData:
            for b in row:
                b = str(b)
                self._getStrWidth(b)
        return self._colWidth

    def _initStr(self, string):
        width = self._getStrWidth(string)
        b = (self.colWidth - width) // 2
        a = (self.colWidth - width) - b
        return f'{" " * a}{string}{" " * b}'

    def __str__(self):
        if not self.rawData:
            return 'console table is empty!'

        data = []
        # 计算每列的最大宽度
        colWidth = [10] * len(self.header)  # 每列的初始宽度
        for i, h in enumerate(self.header):
            colWidth[i] = max(colWidth[i], self._getStrWidth(str(h)))
        for row in self.rawData:
            for i, value in enumerate(row.values()):
                colWidth[i] = max(colWidth[i], self._getStrWidth(str(value)))
        d = []
        for w, value in zip(colWidth, self.header):
            k = self._getStrWidth(str(value))
            b = (w - k) // 2
            a = (w - k) - b
            d.append(f'{" " * a}{value}{" " * b}')
        data.append(d)
        for row in self.rawData:
            d = []
            for w, value in zip(colWidth, row.values()):
                k = self._getStrWidth(str(value))
                b = (w - k) // 2
                a = (w - k) - b
                d.append(f'{" " * a}{value}{" " * b}')
            data.append(d)
        show = [' | '.join(data[0]), '=' * (sum(colWidth) + (3 * (len(self.header) - 1)))]
        for i in data[1:]:
            show.append(' | '.join(i))
        return '\n'.join(show)

    def show(self, message=''):
        logger.info(message + '\n' + str(self.__str__()))


if __name__ == '__main__':
    table = ConsoleTable([{'name': "Tom", 'b': 2}, {'name': "Lucy", 'b': 4}])
    table.show()
    print(table)
    pass
