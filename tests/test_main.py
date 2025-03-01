import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src import main

def test_main():
    main.main()
    
if __name__ == "__main__":
    test_main()
    