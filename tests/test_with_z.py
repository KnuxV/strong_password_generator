from zxcvbn import zxcvbn


# Check the password has at least one lowercase
def test_zxcvbn_score(memorable_password):
    results = zxcvbn(memorable_password)
    score = results["score"]
    assert score == 4

def test_zxcvbn_time(memorable_password):
    results = zxcvbn(memorable_password)
    crack_time = results["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    assert crack_time == "centuries"
