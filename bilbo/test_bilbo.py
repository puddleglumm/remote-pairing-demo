from bilbo import get_bilbo_age


# Bilbo should be eleventy-one :)
def test_get_bilbo_age():
    assert get_bilbo_age() == 111
