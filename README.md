# Générateur de Mots de Passe Sécurisés

Un générateur de mots de passe Python permettant de créer des mots de passe mémorables (basés sur des mots) ou aléatoires (basés sur des caractères).

## Documentation en ligne
[ Lien vers la Dodcumentation ](  https://knuxv.github.io/strong_password_generator  )

## Installation
```bash
# Cloner le dépôt
git clone <votre-repo>
cd testing_username_password


# Installer les dépendances (si génération de documentation)
# pip install pdoc
```

## Utilisation

### Ligne de commande

Générer un mot de passe mémorable de 5 mots :
```bash
python strong_password.py -t memorable -l 5
# Résultat : Stubbed Congress Tiptop Playmate Stagnate
```

Générer un mot de passe aléatoire de 16 caractères :
```bash
python strong_password.py -t random -l 16
# Résultat : aB3$cD9#eF2@gH7!
```

Utiliser la longueur par défaut (12) :
```bash
python strong_password.py -t random
```

### Options

- `-t`, `--type` : Type de mot de passe (requis)
  - `memorable` : Mots de passe composés de mots
  - `random` : Mots de passe composés de caractères aléatoires
- `-l`, `--length` : Longueur du mot de passe (défaut : 12)
  - Pour `memorable` : nombre de mots
  - Pour `random` : nombre de caractères

### Usage programmatique
```python
from strong_password import StrongPassword, TypePassword

# Mot de passe mémorable
gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
password = gen.generate()
print(password)

# Mot de passe aléatoire
gen = StrongPassword(length=16, type_p=TypePassword.RANDOM)
password = gen.generate()
print(password)
```

## Générer la documentation

La documentation est générée automatiquement avec `pdoc`.

### Visualisation locale

Lancer un serveur de documentation avec rechargement automatique :
```bash
pdoc strong_password.py --docformat google
```

Puis ouvrir http://localhost:8080 dans votre navigateur.

### Génération HTML statique

Créer la documentation dans le dossier `docs/` :
```bash
pdoc strong_password.py --docformat google -o docs/
```

### GitHub Pages

La documentation est automatiquement déployée sur GitHub Pages à chaque push sur la branche `main` via GitHub Actions.

URL de la documentation : `https://knuxv.github.io/strong_password_generator`

## Fichiers

- `strong_password.py` : Module principal
- `data/eff_large_wordlist.txt` : Liste de mots EFF pour les mots de passe mémorables
- `.github/workflows/docs.yml` : Configuration GitHub Actions pour la documentation