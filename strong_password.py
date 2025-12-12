import random
from enum import StrEnum, auto

# CONSTANTS
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
char_sets = [LOWERCASE, UPPERCASE, DIGITS, SPECIAL]

with open("data/eff_large_wordlist.txt", "r", encoding="utf-8") as f:
    WORD_LIST = [line.split()[1] for line in f]

class TypePassword(StrEnum):
    """
    Memorable is a series of words, from a dict separated by a space, random is basic string of chars.
    """
    MEMORABLE = auto()
    RANDOM = auto()
    


class StrongPassword:
    def __init__(self, length:int, type_p:TypePassword):
        self.length = length
        self.type_p = type_p

    def generate(self):
        """
        Generates a password based on the specified type.

        The method checks the value of the `type_p` attribute and delegates the
        password generation to the appropriate internal method based on its type.

        :return: A password string generated according to the specified type.
        :rtype: str
        """
        match self.type_p:
            case TypePassword.MEMORABLE:
                return self._generate_memorable()
            case TypePassword.RANDOM:
                return self._generate_random()

    def _generate_memorable(self) -> str:
        """
        Generates a memorable string composed of randomly selected words from a predefined word list.

        This method selects a specific number of words from the ``WORD_LIST`` and joins them together
        with spaces to create a memorable string.

        :return: A memorable string composed of words from ``WORD_LIST``, separated by spaces.
        :rtype: str
        """
        lst_memorable_words : list[str] = random.choices(WORD_LIST, k=self.length)
        return " ".join(lst_memorable_words)

    def _generate_random(self):
        """"""
        password: list[str] = []
        for i in range(self.length):
            # i%4 = 0 or 1 or 2 or 3, we use that to access either Lowercase, Uppercase, Digits or Special
            # When i == 0, we take a lowercase at random
            # When i == 1, we take a Uppercase at ramdom etc...
            password.append(random.choice(char_sets[i%4]))

        # Simple shuffling for extra randomness
        random.shuffle(password)
        return "".join(password)







if __name__ == '__main__':
    a = StrongPassword(length=8, type_p=TypePassword.RANDOM)
    random_password = a.generate()
    print(random_password)


