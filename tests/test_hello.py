import pyhello


def test_hello_world():
    assert pyhello.hello_world() == 'Hello World!'


def test_hello_to():
    for n in ['Alice', 'Bob', 'Charlie']:
        assert pyhello.hello_to(n) == f'Hello {n}'
