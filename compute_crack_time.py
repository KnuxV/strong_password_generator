"""
[SCRIPT] Démo de génération et analyse de mots de passe.

Compare la force de deux types de mots de passe générés aléatoirement.
Utilise zxcvbn pour estimer le temps de craquage.

[USAGE]
    $ python password_strength_demo.py
"""
from zxcvbn import zxcvbn
from strong_password import StrongPassword, TypePassword


def check_password_strength(password: str, password_type: str, length: int) -> None:
    """
    Analyse et affiche la force d'un mot de passe.
    
    Args:
        password: Le mot de passe à analyser.
        password_type: Type du mot de passe ("Memorable" ou "Random").
        length: Longueur (nombre de mots ou caractères).
    """
    results = zxcvbn(password)
    
    score = results["score"]
    crack_time = results["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    
    print(f"\n{password_type} (length={length})")
    print(f"Password: {password}")
    print(f"Score: {score}/4")
    print(f"Crack time: {crack_time}")


def main():
    """Compare deux types de mots de passe générés aléatoirement."""
    # Test 1: Memorable password (4 words)
    memorable_length = 4
    memorable_password = StrongPassword(
        length=memorable_length, 
        type_p=TypePassword.MEMORABLE
    ).generate()
    check_password_strength(memorable_password, "Memorable", memorable_length)
    
    # Test 2: Random password (12 characters)
    random_length = 12
    random_password = StrongPassword(
        length=random_length, 
        type_p=TypePassword.RANDOM
    ).generate()
    check_password_strength(random_password, "Random", random_length)


if __name__ == "__main__":
    main()
