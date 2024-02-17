from deser import describe, serialize, deserialize


class ClassInner:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return describe(self)


class ClassOuter:
    def __init__(self, a, b, c: ClassInner):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.a == other.a and self.b == other.b and self.c == other.c
        return False

    def __repr__(self):
        return describe(self)


def test_serialize():
    v = ClassOuter(1, 'km', ClassInner(2, 'km'))

    assert serialize(1) == 1
    assert serialize(None) == None
    assert serialize('a') == 'a'
    assert serialize(True) == True
    assert serialize(4.5) == 4.5
    assert serialize(v) == {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}
    assert serialize({'x': v}) == {'x': {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}}
    assert serialize([1, 'a', v]) == [1, 'a', {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}]


def test_describe():
    v = ClassOuter(1, 'km', ClassInner(2, 'km'))

    assert describe(1) == '(int) 1'
    assert describe(None) == '(None)'
    assert describe('a') == '(str) a'
    assert describe(True) == '(bool) True'
    assert describe(4.5) == '(float) 4.5'
    assert describe(v) == '(ClassOuter) {a: (int) 1,b: (str) km,c: (ClassInner) {x: (int) 2,y: (str) km}}'
    assert describe({'x': v}) == '{x: (ClassOuter) {a: (int) 1,b: (str) km,c: (ClassInner) {x: (int) 2,y: (str) km}}}'
    assert (describe([1, 'a', v]) ==
            '[(int) 1,(str) a,(ClassOuter) {a: (int) 1,b: (str) km,c: (ClassInner) {x: (int) 2,y: (str) km}}]')


def test_deserialize():
    v = ClassOuter(1, 'km', ClassInner(2, 'km'))

    assert deserialize(1) == 1
    assert deserialize(None) == None
    assert deserialize('a') == 'a'
    assert deserialize(True) == True
    assert deserialize(4.5) == 4.5
    assert deserialize({'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}, ClassOuter) == v

    # note on these cases: we can't autodetect types! so we leave dicts
    assert (deserialize({'x': {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}}) ==
            {'x': {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}})
    assert (deserialize([1, 'a', {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}]) ==
            [1, 'a', {'a': 1, 'b': 'km', 'c': {'x': 2, 'y': 'km'}}])
