import pytest
import os
import time

@pytest.fixture(scope="function") #default = runs once per test file 
def scores():
    print("\n[Building scores fixture]")
    return [88, 77, 92, 67, 71]

@pytest.fixture(scope = "module") # runs once per file, shared across all tests in it
def expensive_setup():
    print("\nexpensive setup fixture, building once for this file")
    return {"connection": "simulated_DB_connection"}

@pytest.fixture(scope="session") # runs once for the entire pytest run, across all files
def global_config():
    print("\nglobal config fixture, built once for the whole test run")
    return {"env" : "test"}

@pytest.fixture
def temp_file():
    print("\ncreating a new file")
    with open("temp.txt" , "w") as f:
        f.write("test data")
    yield "temp.txt"      # pauses here to run the test
    print("\nTeardown : deleting the file")
    os.remove("temp.txt")       # runs after the test is complete; pass or fail.