import pytest
import os
import sys

test_path = os.path.dirname(__file__) + '/test'
sys.path.append(os.path.dirname(__file__) + '/douban_crawler/douban_crawler')

if __name__ == "__main__":
    pytest.main(['-l',  '-rs', '-s', test_path])
