import logging
from src.debug import debug

def test_debug_func_returns_a_func():
    # Arrange
    def test_func():
        pass
    # Act
    result = debug(test_func)
    # Assert
    assert callable(result)

def test_decorated_func_logs_correct_func_name(caplog):
    # Arrange
    caplog.set_level(logging.DEBUG, logger="src.debug")

    @debug
    def do_some_stuff(*args, **kwargs):
        return 'hello!'
    # Act
    do_some_stuff(1, 2, 3, a="a", b="b")
    # Assert
    assert "Function: 'do_some_stuff'" in caplog.text

def test_decorated_func_logs_correct_args(caplog):
    # Arrange
    caplog.set_level(logging.DEBUG, logger="src.debug")

    @debug
    def do_some_stuff(*args, **kwargs):
        return 'hello!'
    # Act
    do_some_stuff(1, 2, 3, a="a", b="b")
    # Assert
    assert "Args: [1, 2, 3]" in caplog.text

def test_decorated_func_logs_correct_kwargs(caplog):
    # Arrange
    caplog.set_level(logging.DEBUG, logger="src.debug")
    
    @debug
    def do_some_stuff(*args, **kwargs):
        return 'hello!'
    # Act
    do_some_stuff(1, 2, 3, a="a", b="b")
    # Assert
    assert "Kwargs: {'a': 'a', 'b': 'b'}" in caplog.text

def test_decorated_func_logs_correct_return_value(caplog):
    # Arrange
    caplog.set_level(logging.DEBUG, logger="src.debug")
    
    @debug
    def do_some_stuff(*args, **kwargs):
        return 'hello!'
    # Act
    do_some_stuff(1, 2, 3, a="a", b="b")
    # Assert
    assert "Return value: hello!" in caplog.text