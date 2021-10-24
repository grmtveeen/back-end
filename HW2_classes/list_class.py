class CustomList(list):
    def __add__(self, other):
        ls = len(self)
        lo = len(other)
        return CustomList([((self[_] if _ < ls else 0) + (other[_] if _ < lo else 0)) for _ in range(max(ls, lo))])

    def __sub__(self, other):
        ls = len(self)
        lo = len(other)
        return CustomList([((self[_] if _ < ls else 0) - (other[_] if _ < lo else 0)) for _ in range(max(ls, lo))])

    def __radd__(self, other):
        ls = len(self)
        lo = len(other)
        return CustomList([((other[_] if _ < lo else 0) + (self[_] if _ < ls else 0)) for _ in range(max(ls, lo))])

    def __rsub__(self, other):
        ls = len(self)
        lo = len(other)
        return CustomList([((other[_] if _ < lo else 0) - (self[_] if _ < ls else 0)) for _ in range(max(ls, lo))])

    def __lt__(self, other):
        return True if sum(self) < sum(other) else False

    def __le__(self, other):
        return True if sum(self) <= sum(other) else False

    def __eq__(self, other):
        return True if sum(self) == sum(other) else False

    def __ne__(self, other):
        return True if sum(self) != sum(other) else False

    def __gt__(self, other):
        return True if sum(self) > sum(other) else False

    def __ge__(self, other):
        return True if sum(self) >= sum(other) else False
