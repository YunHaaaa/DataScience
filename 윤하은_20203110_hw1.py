# 20203110 윤하은 hw1

class Matrix:
    def __init__(self, lst):
        self.data = lst

    def __repr__(self):
        return f"Matrix({self.data})"

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise AssertionError
        tmp = [[] for i in self.data]
        k = 0
        for x, y in zip(self.data, other.data):
            for i, j in zip(x, y):
                tmp[k].append(i+j)
            k += 1
        return Matrix(tmp)

    def __sub__(self, other):
        if len(self.data) != len(other.data):
            raise AssertionError
        tmp = [[] for i in self.data]
        k = 0
        for x, y in zip(self.data, other.data):
            for i, j in zip(x, y):
                tmp[k].append(i-j)
            k += 1
        return Matrix(tmp)

    def __mul__(self, other):
        tmp = [[] for i in self.data]
        if type(other) == Matrix:
            if len(self.data) != len(other.data[0]):
                raise AssertionError
            for a in range(0, len(other.data)-1):
                k = 0
                for x in self.data:
                    sum = 0
                    c = 0
                    for y in other.data:
                        sum += x[c] * y[a]
                        c += 1
                    tmp[k].append(sum)
                    k += 1
            return Matrix(tmp)
        else:
            k = 0
            for x in self.data:
                for i in x:
                    tmp[k].append(i*other)
                k += 1
            return Matrix(tmp)

    def __rmul__(self, other):
        tmp = [[] for i in self.data]
        k = 0
        for x in self.data:
            for i in x:
                tmp[k].append(i * other)
            k += 1
        return Matrix(tmp)
