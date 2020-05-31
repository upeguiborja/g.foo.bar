import solution

def test_solution_1():
    assert solution.solution([2, 0, 2, 2, 0]) == '8'

def test_solution_2():
    assert solution.solution([-2, -3, 4, -5])  == "60"

def test_solution_3():
    assert solution.solution([-1, -1, -1]) == "1"

def test_solution_4():
    assert solution.solution([-1, 2, 2, 9]) == str(2*2*9)

def test_solution_5():
    assert solution.solution([999]) == "999"

def test_solution_6():
    assert solution.solution([-1]) == "-1"

def test_solution_7():
    assert solution.solution([0]) == "0"

def test_solution_7():
    assert solution.solution([1]*50) == "1"

def test_solution_8():
    assert solution.solution([0]*50) == "0"

def test_solution_9():
    assert solution.solution([-1]*50) == "1"

def test_solution_10():
    assert solution.solution([-1]*49) == "1"

def test_solution_11():
    assert solution.solution([1]) == "1"

def test_solution_12():
    assert solution.solution([0,0,0,0,-100]) == "0"


