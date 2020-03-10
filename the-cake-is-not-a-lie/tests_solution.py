import solution

def test_solution_1():
    assert solution.solution("abcabcabcabc") == 4

def test_solution_2():
    assert solution.solution("abccbaabccba") == 2

def test_solution_3():
    assert solution.solution("abcdefabcdef") == 2

def test_solution_4():
    assert solution.solution("") == 0

def test_solution_5():
    assert solution.solution("cabcabcabcab") == 4

def test_solution_6():
    assert solution.solution("bcabcabcabca") == 4

def test_solution_7():
    assert solution.solution("zz") == 2

def test_solution_8():
    assert solution.solution("bccabcbccab") == 0

def test_solution_9():
    assert solution.solution("abcabcabcabc"*20) == 80

def test_solution_10():
    assert solution.solution("a"*200) == 200
