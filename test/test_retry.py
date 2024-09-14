from src.retry import retry

def test_retry_func_returns_a_func():
    result = retry(3)
    assert callable(result)

def test_outer_wrapper_returns_a_func():
    # Arrange
    def test_func():
        pass
    # Act
    outer_wrapper = retry(3)
    result = outer_wrapper(test_func)
    # Assert
    assert callable(result)

def test_decorated_func_is_called():
    # Arrange
    calls = 0

    @retry(3)
    def working_function():
        nonlocal calls
        calls += 1
        return 'SUCCESS'
    # Act
    working_function()
    # Assert
    assert calls == 1

def test_decorated_func_attempted_at_most_num_times():
    # Arrange
    calls = 0

    @retry(3)
    def broken_function():
        nonlocal calls
        calls += 1
        raise Exception('Oh no!')
    # Act
    broken_function()
    # Assert
    assert calls == 3

def test_decorated_func_prints_failure_after_max_attempts(capsys):
    # Arrange
    @retry(3)
    def broken_function():
        raise Exception('Oh no!')
    # Act
    broken_function()
    captured = capsys.readouterr()
    # Assert
    assert captured.out == "FAILURE\n"