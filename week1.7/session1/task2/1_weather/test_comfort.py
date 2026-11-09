# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(15.0) == "COLD" # Tests the boundary condition
    assert comfort_level(-2.6) == "COLD" # Tests a negative

def test_hot():
    assert comfort_level(1000.0) == "HOT"# Tests an extremity
    assert comfort_level(25.1) == "HOT"# Tests the boundary condition

def test_ok():
    assert comfort_level(25.0) == 'OK'# Tests the boundary condition
    assert comfort_level(15.1) == 'OK'# Tests the boundary condition