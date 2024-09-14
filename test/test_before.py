from src.before import before

def test_before_func_returns_a_func():
    result = before(2)
    assert callable(result)

def test_outer_wrapper_returns_a_func():
    # Arrange
    def test_func():
        pass

    outer_wrapper = before(2)
    # Act
    result = outer_wrapper(test_func)
    # Assert
    assert callable(result)

def test_decorated_function_is_called():
    # Arrange
    calls = 0

    @before(2)
    def greet():
        nonlocal calls
        calls += 1
        return 
    # Act
    greet()
    # Assert
    assert calls == 1 

def test_decorated_function_is_called_no_more_than_num_minus_1_times():
    # Arrange
    calls = 0

    @before(3)
    def greet():
        nonlocal calls
        calls += 1
        return "Hello there!"
    # Act
    greet()
    greet()
    greet()
    # Assert
    assert calls == 2

def test_returns_none_after_decorated_func_called_max_num_times():
    # Arrange
    @before(3)
    def greet():
        return "Hello there!"
    # Act 
    result = greet()
    # Assert
    assert result == "Hello there!"
    assert greet() == "Hello there!"
    assert greet() == None
    assert greet() == None