from arithmetic import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0  

def test_divide():  
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0
    assert divide(1, 0) == "Error: Division by zero is not allowed."