# So we can access the utility files:
import sys
sys.path.append('../')

# The main library:
from get_data import get_data

# The test:
def test_get_data():
    # This is the case where the file doesn't exist, so it returns an empty dictionary.
    # The not key word effectively means "there is nothing in there" or length 0.
    empty_results = get_data('obviously wrong filename.csv')
    assert not empty_results

    # Now we use data that I corrupted, removing the time column.  This will
    # return an empty dictionary.  
    wrong_results = get_data('../../data/corrupted_sample.csv')
    assert not wrong_results

    # Now we use real data.  This should return a dictionary.
    real_results = get_data('../../data/sample_1.csv')
    assert real_results

    # We can also assert that they're dictionaries in all cases:
    assert(type(empty_results) == dict)
    assert(type(wrong_results) == dict)
    assert(type(real_results) == dict)
