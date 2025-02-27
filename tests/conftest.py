import pytest
import logging

@pytest.fixture(autouse=True)
def setup_and_teardown():
    #logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    print("")
    print(".. STR ........................................................................")  
    yield
    # Teardown code, one point less becuase of existing point
    print(". FIN ........................................................................")  