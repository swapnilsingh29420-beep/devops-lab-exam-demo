from facotrial import fact

def test_fact():
  assert fact(3) == 6
  assert fact(5) == 120
  assert fact(0) == 1
