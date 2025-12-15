def test_length_memorable(memorable_password):
    assert len(memorable_password) > 20


def test_lowercase(memorable_password):
    assert any(char.islower() for char in memorable_password)


def test_uppercase(memorable_password):
    assert any(char.isupper() for char in memorable_password)


def test_has_spaces(memorable_password):
    assert memorable_password.count(" ") >= 4
