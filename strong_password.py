"""
[MODULE] Générateur de mots de passe sécurisés.

Deux types de génération :
- MEMORABLE : mots aléatoires de la liste EFF (ex: "Stubbed Congress Tiptop")
- RANDOM : caractères variés (ex: "aB3$cD9#eF2@")

[USAGE CLI]
    $ python strong_password.py -t memorable -l 5
    $ python strong_password.py -t random -l 16

[USAGE CODE]
    >>> gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
    >>> password = gen.generate()
"""

import argparse
import random
from enum import StrEnum, auto

# CONSTANTS
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
char_sets = [LOWERCASE, UPPERCASE, DIGITS, SPECIAL]

with open("data/eff_large_wordlist.txt", "r", encoding="utf-8") as f:
    WORD_LIST = [line.split()[1].capitalize() for line in f]


class TypePassword(StrEnum):
    """
    [ENUM] Types de mots de passe disponibles.

    Attributes:
        MEMORABLE: Mots aléatoires de la EFF wordlist (ex: "Stubbed Congress").
        RANDOM: Caractères variés avec minuscules, majuscules, chiffres, spéciaux.
    """
    MEMORABLE = auto()
    RANDOM = auto()


class StrongPassword:
    """
    [CLASSE] Générateur de mots de passe sécurisés.

    Attributes:
        length (int): Nombre de mots (MEMORABLE) ou caractères (RANDOM).
        type_p (TypePassword): Type de génération (MEMORABLE ou RANDOM).

    Example:
        >>> gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
        >>> password = gen.generate()
    """

    def __init__(self, length: int, type_p: TypePassword):
        """Initialise le générateur."""
        self.length = length
        self.type_p = type_p

    def generate(self) -> str:
        """
        Génère le mot de passe selon le type spécifié.

        Returns:
            str: Le mot de passe généré.
        """
        match self.type_p:
            case TypePassword.MEMORABLE:
                return self.generate_memorable()
            case TypePassword.RANDOM:
                return self.generate_random()
            case _:
                raise ValueError(f"Type de mot de passe non reconnu : {self.type_p}")

    def generate_memorable(self) -> str:
        """
        Génère un mot de passe mémorable (mots aléatoires).

        Sélectionne des mots depuis la EFF Large Wordlist (7776 mots).
        Chaque mot commence par une majuscule.

        Returns:
            str: Mots séparés par des espaces (ex: "Stubbed Congress Tiptop").
        """
        lst_memorable_words: list[str] = random.choices(WORD_LIST, k=self.length)
        return " ".join(lst_memorable_words)

    def generate_random(self) -> str:
        """
        Génère un mot de passe aléatoire (caractères variés).

        Alterne cycliquement entre 4 types de caractères puis mélange le résultat.
        Garantit au moins un caractère de chaque type si length >= 4.

        Returns:
            str: Caractères aléatoires (ex: "aB3$cD9#eF2@").
        """
        password: list[str] = []
        for i in range(self.length):
            # Cycle : minuscule (0) → majuscule (1) → chiffre (2) → spécial (3)
            password.append(random.choice(char_sets[i % 4]))
        random.shuffle(password)
        return "".join(password)


def main() -> None:
    """
    [CLI] Point d'entrée pour la ligne de commande.

    Arguments:
        -l, --length: Nombre de mots ou caractères (défaut: 12).
        -t, --type: Type 'memorable' ou 'random' (requis).

    Example:
        $ python strong_password.py -t memorable -l 5
    """
    parser = argparse.ArgumentParser(
        prog="StrongPasswordGenerator",
        description="Génère des mots de passe sécurisés."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Nombre de mots (memorable) ou caractères (random). Défaut: 12"
    )
    parser.add_argument(
        "-t", "--type",
        choices=[e.value for e in TypePassword],
        required=True,
        help="Type : 'memorable' (mots) ou 'random' (caractères)"
    )

    args = parser.parse_args()
    print(
        StrongPassword(length=args.length, type_p=args.type).generate()
    )


if __name__ == '__main__':
    main()
