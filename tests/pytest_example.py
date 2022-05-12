import pytest
from jsonschema import validate
"""
schema = {

    "type" : "string",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}
"""
# validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

@pytest.mark.parametrize("input,expected", [
    pytest.param(7,7, marks=pytest.mark.positive, id='positive1'),
    pytest.param(7,9, marks=pytest.mark.negative, id='negative1')])
def test_add(input, expected):
    assert input == expected