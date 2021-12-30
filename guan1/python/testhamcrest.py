from hamcrest import *

assert_that(10, equal_to(9))
print('1111')
assert_that(10, close_to(9, 1), '2222')
print('3333')
