from Cope.debugging import *
# from Cope.debugging import Debug as debug

def test_debug():
    debug('test')


    @debug
    def test():
        print('test called')

    test()

    @debug
    class Test:
        def __init__(self):
            print('Test initialized')

    Test()

    def test2():
        print('test2 called')

    debug(test2)
    debug(1)
    debug()
    var = 6
    debug(var)

test_debug()
