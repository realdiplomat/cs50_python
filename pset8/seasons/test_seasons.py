import seasons
from datetime import date


def test_validity():
    valid_dob = seasons.Date(date(1999,1,1))
    assert valid_dob.dob.year == 1999
    assert valid_dob.dob.month == 1
    assert valid_dob.dob.day == 1
