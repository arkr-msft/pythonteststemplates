
# create documentation

# create a test that fails
def test_long_dictionaries():
  result = {'key': 'value', 'lastname': 'kumar', 'firstname': 'arun'}
  expected = {'key': 'value', 'lastame': 'kumar', 'firstname': 'arun'}
  assert result == expected

# run the test via the command line using following command
# pytest asserts/test_long_dictionaries.py
