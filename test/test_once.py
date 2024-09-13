from src.once import once

def test_returns_a_function():
    # Arrange
    def do_some_stuff():
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    # Assert
    assert callable(result)

def test_decorated_func_called_once():
    # Arrange
    calls = 0

    def do_some_stuff():
        nonlocal calls
        calls += 1
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    result()
    # Assert
    assert calls == 1

def test_decorated_func_is_called_once():
    # Arrange
    calls = 0

    def do_some_stuff():
        nonlocal calls
        calls += 1
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    result()
    # Assert
    assert calls == 1

def test_decorated_func_called_only_once():
    # Arrange
    calls = 0

    def do_some_stuff():
        nonlocal calls
        calls += 1
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    result()
    result()
    result()
    # Assert
    assert calls == 1

def test_decorated_func_returns_correct_output():
    # Arrange
    def do_some_stuff():
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    # Assert
    assert result() == "Would you look at that, I've been invoked!"

def test_decorated_func_returns_none_after_first_call():
    # Arrange
    def do_some_stuff():
        return "Would you look at that, I've been invoked!"
    # Act
    result = once(do_some_stuff)
    # Assert
    assert result() == "Would you look at that, I've been invoked!"
    assert result() == None
    assert result() == None
    assert result() == None