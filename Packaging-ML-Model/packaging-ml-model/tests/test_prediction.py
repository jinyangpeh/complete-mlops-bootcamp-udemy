'''
Pytest will run all files of the form test_*.py or *_test.py in the current directory
and its subdirectories.
'''
import pytest

from pathlib import Path
import os
import sys

# Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# output from predict script not null
# output from predict script is str data type
# the output is Y for an example data

#Fixtures --> functions before test function --> ensure single_prediction

# Ensures that the single_prediction() function is ran before all test functions
# Pytest will run all functions that start with test_*
@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

def test_single_pred_not_none(single_prediction): # output is not none
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction): # data type is string
    assert isinstance(single_prediction.get('prediction')[0],str)

def test_single_pred_validate(single_prediction): # check the output is Y
    assert single_prediction.get('prediction')[0] == 'Y'