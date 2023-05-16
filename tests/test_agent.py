# test_param.py 

import pytest
from tests.CheckEnv import check_pytest
@pytest.fixture(scope="session")
def name(pytestconfig):
    return pytestconfig.getoption("name")

def test_print_name(name):
    print(f"\ncommand line param (name): {name}")
    Bool_check = check_pytest(name)[0]
    print(Bool_check)
