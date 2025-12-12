"""
Générateur de mots de passe sécurisés.

Ce module fournit des outils pour générer des mots de passe robustes selon deux
approches : mémorables (basés sur des mots) ou aléatoires (basés sur des caractères).

Le générateur mémorable utilise la liste de mots EFF (Electronic Frontier Foundation)
pour créer des phrases faciles à retenir mais difficiles à deviner. Le générateur
aléatoire crée des mots de passe alphanumériques avec caractères spéciaux en
garantissant la présence de chaque type de caractère.

Usage en ligne de commande:
    Générer un mot de passe mémorable de 5 mots:

        $ python strong_password.py -t memorable -l 5
        Stubbed Congress Tiptop Playmate Stagnate

    Générer un mot de passe aléatoire de 16 caractères:

        $ python strong_password.py -t random -l 16
        aB3$cD9#eF2@gH7!

    Utiliser la longueur par défaut (12):

        $ python strong_password.py -t random

Usage programmatique:
    >>> from strong_password import StrongPassword, TypePassword
    >>> gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
    >>> password = gen.generate()
    >>> print(password)
    Stubbed Congress Tiptop Playmate Stagnate

Attributes:
    LOWERCASE (str): Ensemble des lettres minuscules.
    UPPERCASE (str): Ensemble des lettres majuscules.
    DIGITS (str): Ensemble des chiffres.
    SPECIAL (str): Ensemble des caractères spéciaux autorisés.
    WORD_LIST (list[str]): Liste de mots issus de la EFF Large Wordlist.
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
    Énumération des types de mots de passe disponibles.

    Cette énumération définit deux stratégies de génération de mots de passe
    avec des compromis différents entre sécurité et mémorabilité.

    Attributes:
        MEMORABLE: Génère un mot de passe composé de mots aléatoires issus de la
            EFF wordlist. Plus facile à retenir mais généralement plus long
            (ex: "Stubbed Congress Tiptop").
        RANDOM: Génère un mot de passe composé de caractères aléatoires incluant
            minuscules, majuscules, chiffres et caractères spéciaux. Plus court
            mais plus difficile à mémoriser (ex: "aB3$cD9#").
    """
    MEMORABLE = auto()
    RANDOM = auto()


class StrongPassword:
    """
    Générateur de mots de passe sécurisés.

    Cette classe permet de créer des mots de passe robustes selon deux approches
    paramétrables : des mots de passe mémorables (basés sur des mots) ou aléatoires
    (basés sur des caractères). La longueur est configurable selon les besoins.

    Attributes:
        length (int): Pour MEMORABLE, nombre de mots à générer. Pour RANDOM, nombre
            de caractères à générer.
        type_p (TypePassword): Type de mot de passe à générer (MEMORABLE ou RANDOM).

    Examples:
        Générer un mot de passe mémorable:

            >>> gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
            >>> password = gen.generate()
            >>> print(password)
            Stubbed Congress Tiptop Playmate Stagnate

        Générer un mot de passe aléatoire:

            >>> gen = StrongPassword(length=16, type_p=TypePassword.RANDOM)
            >>> password = gen.generate()
            >>> print(password)
            aB3$cD9#eF2@gH7!
    """

    def __init__(self, length: int, type_p: TypePassword):
        """
        Initialise le générateur de mot de passe.

        Args:
            length (int): Nombre de mots (pour MEMORABLE) ou de caractères (pour RANDOM).
                Doit être un entier positif.
            type_p (TypePassword): Type de génération à utiliser (MEMORABLE ou RANDOM).
        """
        self.length = length
        self.type_p = type_p

    def generate(self) -> str:
        """
        Génère le mot de passe selon le type spécifié.

        Délègue la génération à la méthode privée appropriée en fonction du
        type de mot de passe choisi lors de l'initialisation.

        Returns:
            str: Le mot de passe généré sous forme de chaîne de caractères.

        Raises:
            ValueError: Si le type de mot de passe est invalide (ne devrait
                jamais arriver avec l'énumération TypePassword).
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
        Génère un mot de passe mémorable composé de mots aléatoires.

        Sélectionne aléatoirement des mots depuis la EFF Large Wordlist (liste
        de 7776 mots optimisée pour la génération de mots de passe) et les
        assemble avec des espaces. Chaque mot commence par une majuscule pour
        faciliter la saisie et la lisibilité.

        Returns:
            str: Mot de passe composé de mots séparés par des espaces, chaque
                mot commençant par une majuscule.

        Examples:
            >>> # Avec length=4
            >>> password = self.generate_memorable()
            >>> print(password)
            Stubbed Congress Tiptop Playmate

        Note:
            La sélection utilise `random.choices` qui permet les répétitions.
            Pour un mot de passe de 5 mots, l'entropie est d'environ 64.6 bits
            (log2(7776^5)).
        """
        lst_memorable_words: list[str] = random.choices(WORD_LIST, k=self.length)
        return " ".join(lst_memorable_words)

    def generate_random(self) -> str:
        """
        Génère un mot de passe aléatoire de caractères variés.

        Construit un mot de passe en alternant cycliquement entre quatre ensembles
        de caractères (minuscules, majuscules, chiffres, caractères spéciaux) pour
        garantir la présence de chaque type. Le résultat est ensuite mélangé
        aléatoirement pour masquer ce pattern cyclique.

        Returns:
            str: Mot de passe composé de caractères aléatoires incluant au moins
                un caractère de chaque type (si length >= 4).

        Examples:
            >>> # Avec length=12
            >>> password = self.generate_random()
            >>> print(password)
            aB3$cD9#eF2@

        Note:
            Pour length >= 4, le mot de passe contient obligatoirement au moins :
            - 1 lettre minuscule
            - 1 lettre majuscule
            - 1 chiffre
            - 1 caractère spécial

            Le mélange final (shuffle) empêche de deviner l'ordre des types de
            caractères et renforce la sécurité.
        """
        password: list[str] = []
        for i in range(self.length):
            # i%4 = 0 ou 1 ou 2 ou 3, utilisé pour accéder cycliquement aux ensembles
            # i == 0 → minuscule, i == 1 → majuscule, i == 2 → chiffre, i == 3 → spécial
            # i == 4 → i % 4 == 0, on revient aux minuscules
            password.append(
                random.choice(char_sets[i % 4])
            )
        # Mélange pour masquer le pattern cyclique
        random.shuffle(password)
        return "".join(password)


def main() -> None:
    """
    Point d'entrée pour l'interface en ligne de commande.

    Parse les arguments de la ligne de commande et génère un mot de passe selon
    les paramètres fournis par l'utilisateur. Le mot de passe généré est affiché
    sur la sortie standard (stdout).

    Arguments de ligne de commande:
        -l, --length (int): Longueur du mot de passe.
        Pour MEMORABLE, c'est le nombre de mots.
        Pour RANDOM, c'est le nombre de caractères.
        Valeur par défaut : 12.

        -t, --type (str): Type de mot de passe à générer. Choix obligatoire
            entre 'memorable' (mots) ou 'random' (caractères).

    Examples:
        Générer 5 mots mémorables:

            $ python strong_password.py -t memorable -l 5
            Stubbed Congress Tiptop Playmate Stagnate

        Générer 16 caractères aléatoires:

            $ python strong_password.py -t random -l 16
            aB3$cD9#eF2@gH7!

        Utiliser la longueur par défaut (12 caractères):

            $ python strong_password.py -t random
            aB3$cD9#eF2@

    Raises:
        SystemExit: Si les arguments sont invalides ou manquants, argparse
            affiche un message d'erreur et termine le programme.
    """
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(
        prog="StrongPasswordGenerator",
        description="Génère des mots de passe sécurisés mémorables ou aléatoires."
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
        help="Type de mot de passe : 'memorable' (mots) ou 'random' (caractères)"
    )

    # Récupération des arguments utilisateur
    args = parser.parse_args()
    user_length = args.length
    user_type = args.type

    # Génération et affichage du mot de passe
    print(
        StrongPassword(length=user_length, type_p=user_type).generate()
    )


if __name__ == '__main__':
    main()
