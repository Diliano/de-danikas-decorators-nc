from src.do_twice import do_twice

def test_returns_a_function():
    # Arrange
    def quick_maths():
        2 + 2 - 1 == 3
    # Act
    result = do_twice(quick_maths)
    # Assert
    assert callable(result)

def test_decorated_func_called_twice():
    # Arrange
    calls = 0

    def quick_maths():
        nonlocal calls
        calls += 1
        2 + 2 - 1 == 3
    # Act
    result = do_twice(quick_maths)
    result()
    # Assert
    assert calls == 2