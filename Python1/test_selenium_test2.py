import python2_test2

#判定
def test_leap_check():
    year1 = 2020
    year2 = 2019
    value = python2_test2.leap_check(year1)
    assert value == True
    value = python2_test2.leap_check(year2)
    assert value == False