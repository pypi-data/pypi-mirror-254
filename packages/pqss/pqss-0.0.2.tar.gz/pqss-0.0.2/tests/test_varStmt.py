import pqss


def test_mixin_parsing():
    tests = [('$a : 5; MyClass { width: $a; &:hover { width: $a + 3 * 5; &::indicator { width: $a + 3 * 5; } } } }', '$a', True)]
    for test in tests:
        qss = pqss.compile_pqss(test[0])
        print(qss)
