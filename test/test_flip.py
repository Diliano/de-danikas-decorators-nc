from src.flip import flip

def test_returns_a_function():
    # Arrange
    def divide(a, b):
        return a / b
    # Act
    result = flip(divide)
    # Assert
    assert callable(result)

def test_calls_decorated_function():
    # Arrange
    calls = 0

    def divide(a, b):
        nonlocal calls
        calls += 1
        return a / b
    # Act
    result = flip(divide)
    result(4, 2)
    # Assert
    assert calls == 1

def test_flips_two_arguments():
    # Arrange
    @flip
    def divide(a, b):
        return a / b
    # Act + Assert
    assert divide(4, 2) == 0.5

def test_flips_multiple_args():
    # Arrange
    @flip
    def join_words(*args):
        return (" ").join(args)
    
    test_input = ("friends", "morning", "good")
    # Act + Assert
    assert join_words(*test_input) == "good morning friends"

def test_handles_single_arg():
    # Arrange
    @flip
    def test_func(arg):
        return arg
    # Act
    result = test_func(5)
    # Assert
    assert result == 5