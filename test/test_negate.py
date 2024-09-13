from src.negate import negate

def test_returns_a_function():
    # Arrange
    def does_this_return_true():
        return True
    # Act
    result = negate(does_this_return_true)
    # Assert
    assert callable(result)

def test_decorator_returns_boolean():
    # Arrange
    @negate 
    def does_this_return_true():
        return True
    # Act
    result = does_this_return_true()
    # Assert
    assert type(result) == bool

def test_decorator_returns_flipped_boolean():
    # Arrange
    @negate 
    def does_this_return_true():
        return True
    # Act
    result = does_this_return_true()
    # Assert
    assert result == False