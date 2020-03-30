from solution import solution

def test_solution_1():
    assert solution([1, 1, 1]) == 1

def test_solution_2():
    assert solution([1, 2, 3, 4, 5, 6]) == 3

def test_solution_3():
    assert solution([1, 1, 1, 1, 1, 1]) == 20

def test_solution_4():
    assert solution([1, 1]) == 0

def test_solution_5():
    assert solution([6, 5, 4, 3, 2, 1]) == 0

def test_solution_6():
    assert solution([1, 1, 1, 1]) == 4

def test_solution_7():
    assert solution([1, 2 ,4 ,8]) == 4

def test_solution_8():
    assert solution([1, 2, 4, 6, 12]) == 7

def test_solution_9():
    assert solution(list(range(1, 2001))) == 40888

def test_solution_10():
    assert solution([1, 5, 6]) == 0