from src.convert_type import convert_type

def test_convert_type_returns_a_function():
    result = convert_type(set)
    assert callable(result)

def test_outer_wrapper_returns_a_function():
    #Arrange
    def test_func():
        pass
    #Act
    result = convert_type(set)
    # Assert
    assert callable(result(test_func))

def test_decorated_func_is_called():
    # Arrange
    calls = 0

    @convert_type(set)
    def create_simple_list():
        nonlocal calls
        calls += 1
        return [1, 1, 2, 2, 3, 4, 5, 5, 5]
    # Act
    create_simple_list()
    # Assert
    assert calls == 1

def test_decorated_func_returns_desired_type():
    # Arrange 
    @convert_type(set)
    def create_simple_list():
        return [1, 1, 2, 2, 3, 4, 5, 5, 5]
    
    expected = {1, 2, 3, 4, 5}
    # Act
    result = create_simple_list()
    # Assert
    assert result == expected