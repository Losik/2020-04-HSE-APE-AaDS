import time


def decorator(func):

    # Declaring a measures execution time of a func
    # with provided arguments
    def decorated(*args, **kwargs):
        st = time.time()
        value = func(*args, **kwargs)
        print(f'elapsed time is {1000 * (time.time() - st):0.3f} milliseconds')
        return value

    return decorated


@decorator
def foo(a, b, c):
    print(f'a={a} b={b} c={c}')


@decorator
def bar(x, y, *args, a=None, b=None, **kwargs):
    print(f'x={x}, y={y}, args={args} a={a}, b={b}, kwargs={kwargs}')


foo(1, 2, 3)
bar(1, *[2, 3], a=4, **{'b': 5, 'c': 6})
