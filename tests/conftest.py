import pytest
from strong_password import StrongPassword, TypePassword


# We generate a random password as a fixture that we can use in test
@pytest.fixture
def random_password():
    random_p = StrongPassword(length=12, type_p=TypePassword.RANDOM).generate()
    return random_p


@pytest.fixture
def memorable_password():
    mem_p = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    return mem_p
