"""field len"""
F_LEN = 3


class TicTac:
    """Tic tac class game"""

    def __init__(self):
        self.__field = [['_' for _ in range(F_LEN)] for _ in range(F_LEN)]

    def start_game(self):
        """Method that starts game"""
        symbol = 'X'
        for _ in range(F_LEN ** 2):
            self.info()
            print('Введите i j для игрока ' + symbol, end=' ')
            while True:
                try:
                    i, j = map(int, input().split())
                    self.put(symbol, i, j)
                except ValueError as z_err:
                    print(str(z_err) + ', введите данные ещё раз', end=' ')
                else:
                    break
            if self.check(symbol):
                print('Игрок ' + symbol + ' победил!')
                self.info()
                break
            if symbol == 'X':
                symbol = '0'
            else:
                symbol = 'X'
        else:
            print('Ничья :(')

    def put(self, symbol, i, j):
        """Method puts X or 0 on field"""
        if self.validate(symbol, i, j):
            self.__field[i][j] = symbol

    def check(self, symbol):
        """Method check win"""
        if self.validate(symbol):
            example = [symbol for _ in range(F_LEN)]
            for i in range(F_LEN):
                if self.__field[i] == example:
                    return True
                if [self.__field[i][j] for j in range(F_LEN)] == example:
                    return True
            if example in ([self.__field[i][i] for i in range(F_LEN)],
                           [self.__field[i][F_LEN-1-i] for i in range(F_LEN)]):
                return True
            return False

    def info(self):
        """Method printing field"""
        for i in range(F_LEN):
            print('|'.join(self.__field[i]))

    def validate(self, symbol, i=None, j=None):
        """Method check validate"""
        if symbol not in ('X', '0'):
            raise ValueError('Попытка записи на поле не X или 0')
        if i is not None and j is not None:
            if i not in range(F_LEN) or j not in range(F_LEN):
                raise ValueError('Выход за пределы поля')
            if self.__field[i][j] != '_':
                raise ValueError('Попытка перезаписи символа')
        return True


if __name__ == '__main__':
    game = TicTac()
    game.start_game()
