from hello import add

assert add(0, 0) == 0
assert add(12, 12) == 24
assert add(-12, 12) == 0
assert add(12, -2) == 10
assert add(-12, -2) == -14
