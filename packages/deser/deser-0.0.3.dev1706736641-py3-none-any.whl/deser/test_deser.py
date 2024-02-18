from typing import List, Dict

from deser import describe, serialize, deserialize, validate


class ClassInner:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return describe(self)


class ClassOuter:
    def __init__(self, a: float, b: float, c: ClassInner):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.a == other.a and self.b == other.b and self.c == other.c
        return False

    def __repr__(self):
        return describe(self)


class ClassWithoutConstructor:
    pass


class ClassWithoutTypeHint:
    def __init__(self, x):
        self.x = x


class ClassWithIncompatibleTypeHint:
    def __init__(self, x: dict):
        self.x = x


def test_validate():
    assert validate(ClassWithoutConstructor) == False
    assert validate(ClassWithoutTypeHint) == False
    assert validate(ClassWithIncompatibleTypeHint) == False
    assert validate(list) == False
    assert validate(List) == False
    assert validate(List[dict]) == False
    assert validate(dict) == False
    assert validate(Dict) == False
    assert validate(Dict[int, int]) == False

    assert validate(int) == True
    assert validate(str) == True
    assert validate(bool) == True
    assert validate(float) == True
    assert validate(List[int]) == True
    assert validate(List[str]) == True
    assert validate(List[bool]) == True
    assert validate(List[float]) == True
    assert validate(Dict[str, float]) == True
    assert validate(Dict[str, str]) == True
    assert validate(Dict[str, bool]) == True
    assert validate(Dict[str, float]) == True
    assert validate(ClassInner) == True
    assert validate(ClassOuter) == True
    assert validate(List[ClassOuter]) == True
    assert validate(Dict[str, ClassOuter]) == True
    assert validate(Dict[str, List[ClassOuter]]) == True


def test_serialize():
    v = ClassOuter(1, 2.0, ClassInner(2, 4))

    assert serialize(1) == 1
    assert serialize(None) == None
    assert serialize('a') == 'a'
    assert serialize(True) == True
    assert serialize(4.5) == 4.5
    assert serialize(v) == {'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}
    assert serialize({'x': v}) == {'x': {'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}}
    assert serialize([1, 'a', v]) == [1, 'a', {'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}]


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
    v = ClassOuter(1, 2.0, ClassInner(2, 4))

    assert deserialize(1, int) == 1
    assert deserialize(None, int) == None
    assert deserialize('a', str) == 'a'
    assert deserialize(True, bool) == True
    assert deserialize(4.5, float) == 4.5
    assert deserialize({'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}, ClassOuter) == v
    assert deserialize([{'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}], List[ClassOuter]) == [v]
    assert deserialize({'x': {'a': 1, 'b': 2.0, 'c': {'x': 2, 'y': 4}}}, Dict[str, ClassOuter]) == {'x': v}
