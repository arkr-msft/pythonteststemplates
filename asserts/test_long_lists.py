#create a test that fails
def test_long_lists():
  result = ['this', 'is', 'a', 'list', 'with', 'tons', 'of', 'items']
  expected = ['this', 'is', 'A', 'list', 'with', 'tons', 'of', 'items']
  assert result == expected

  # run the test via the command line using following command
  # pytest asserts/test_long_lists.py