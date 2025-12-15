from strong_password import StrongPassword, TypePassword
# ============================================================================
# TESTS AVEC FIXTURES (réutilisation de mots de passe pré-générés)
# ============================================================================


# Check the password is more than 20 characters long
def test_length_memorable(memorable_password):
    assert len(memorable_password) > 20


# Check the password has at least one lowercase
def test_lowercase(memorable_password):
    assert any(char.islower() for char in memorable_password)


# Check it has at least one uppercase
def test_uppercase(memorable_password):
    assert any(char.isupper() for char in memorable_password)


# Check if the password has more than 3 words
def test_has_spaces(memorable_password):
    assert memorable_password.count(" ") >= 4


# ============================================================================
# TESTS DIRECTS (génération à la demande, sans fixtures)
# ============================================================================


def test_length_memorable_direct():
    password = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    assert len(password) > 20


def test_lowercase_direct():
    password = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    assert any(char.islower() for char in password)


def test_uppercase_direct():
    password = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    assert any(char.isupper() for char in password)


def test_has_spaces_direct():
    password = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    assert password.count(" ") >= 4
