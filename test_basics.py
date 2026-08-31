import pytest
import os
import time

# Step 1 — What pytest actually does (15 min)
# Pytest finds and runs functions that start with test_, 
# and uses Python's plain assert keyword to check results. That's it — no special syntax needed for a basic test.

def add (a,b):
    return a+b

def test_add_two_numbers():
    assert add(2,3) == 5

def test_add_two_negative_numbers():
    assert add(-1, -1) == -2

    
# Step 2 — The problem that fixtures solve (15 min)

# Say you're testing something that needs setup first — like a list of test data you need in every test: 

def test_scores_average():
    scores = [88, 77, 92, 67, 71] # setup, repeated every time
    assert sum(scores)/ len(scores) == 79


def test_scores_max():
    scores = [88, 77, 92, 67, 71] # same setup, copy-pasted again
    assert max(scores) == 92

# Copying that scores = [...] line into every test is exactly what fixtures exist to eliminate.


# Step 3 — What a decorator is, in one minimal example (15 min)

# You need just enough decorator understanding to read @pytest.fixture. 
# A decorator is a function that wraps another function to add behavior, using @ syntax:
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())

# You don't need to write decorators yourself for a while — you just need to recognize that 
# @something above a function means "this function is being wrapped/modified by something." That's all pytest fixtures use this for.



# Step 4 — Your first fixture (20 min)

@pytest.fixture
def scores():
    return [88, 77, 92, 67, 71]

def test_scores_average(scores):
    assert sum(scores)/len(scores) == 79

def test_scores_max(scores):
    assert max(scores) == 92

# Notice: the parameter name scores in each test function matches the fixture's function name. 
# Pytest sees that match and automatically calls the fixture, then passes its return value in. 

# Step 5 — Fixture scope: the actual concept for today's task (30 min)

# By default, a fixture runs fresh for every single test function that uses it — 
# that's scope="function", the default. But sometimes rebuilding the same setup for every test is wasteful. 
# Scope controls how often the fixture reruns:

@pytest.fixture(scope="function") #default = runs once per test file 
def scores():
    print("\nBuilding scores fixture")
    return [88, 77, 92, 67, 71]

@pytest.fixture(scope = "module") # runs once per file, shared across all tests in it
def expensive_setup():
    print("\nexpensive setup fixture, building once for this file")
    return{"connection : simulated_DB_connection"}

@pytest.fixture(scope="session") # runs once for the entire pytest run, across all files
def global_config():
    print("\nglobal config fixture, built once for the whole test run")
    return {"env" : "test"}

# function (default) — use when tests might modify the data and shouldn't affect each other (test isolation)
# class — share setup across tests grouped in one class
# module — share expensive setup (like a database connection) across every test in one file
# session — share setup across your entire test run — use for things that are truly global and expensive, like spinning up a test server once

# Step 6 — Yield fixtures: setup AND teardown (25 min)
@pytest.fixture
def temp_file():
    print("\ncreating a new file")
    with open("temp.txt" , "w") as f:
        f.write("test data")
    yield "temp.txt"      # pauses here to run the test
    print("\nTeardown : deleting the file")
    os.remove("temp.txt")       # runs after the test is complete; pass or fail.

def test_file_has_content(temp_file):
    with open(temp_file) as f:
        assert f.read() == "test data"

# Everything before yield is setup. Everything after is teardown — 
# and it runs even if the test fails, which matters for cleanup like closing connections or deleting test data.

@pytest.fixture(scope= "module")
def expensive_connection():
    print("\n[connecting.. this takes 2 seconds]")
    time.sleep(2)
    return{"status" :"connected"}   

def test_one(expensive_connection):
    assert expensive_connection["status"] == "connected"

def test_two(expensive_connection):
    assert expensive_connection["status"] == "connected"

def test_three(expensive_connection):
    assert expensive_connection["status"] == "connected"


@pytest.fixture
def temp_file():
    print("\n[SETUP] creating a new file")
    with open("test.txt" , "w") as f:
        f.write("sample test data")
    yield "test.txt"
    print("\n[TEARDOWN] Deleting temp file")
    os.remove("test.txt")

def test_temp_file(temp_file):
    with open(temp_file) as f:
        assert f.read() == "sample test data"