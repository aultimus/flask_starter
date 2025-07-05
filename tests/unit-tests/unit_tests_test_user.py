from flask_starter.user import foo


def test_foo():
    result = foo()
    assert result == 1
