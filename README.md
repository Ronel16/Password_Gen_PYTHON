# Générateur et Testeur de Mot de Passe

Ce projet est un outil de sécurité permettant de générer et tester des mots de passe, incluant :
- Génération de mots de passe aléatoires personnalisables
- Génération de passphrases avec la méthode des dés de l'EFF
- Test de force des mots de passe

## Fonctionnalités

- **🔍 Test de mots de passe**
  - Analyse de la composition (minuscules, majuscules, chiffres, caractères spéciaux)
  - Évaluation de la force

- **🎲 Génération de mots de passe**
  - Choix du nombre de caractères de chaque type
  - Mélange aléatoire
  - Évaluation automatique de la force

- **🎯 Génération de passphrase**
  - Utilisation de la liste de mots de l'EFF
  - Méthode des dés pour une génération aléatoire sécurisée
  - Instructions pour utiliser des dés physiques

## Installation

1. Cloner le repository :
```bash
git clone https://github.com/Ronel16/Password_Gen_PYTHON.git
cd Password_Gen_PYTHON
```

2. Vérifier que tous les fichiers sont présents :
- password_checker.py
- password_generator.py
- passphrase_generator.py
- test_unitaire.py
- test_password.py
- main.py
- eff_large_wordlist.txt

## Utilisation

Lancer le programme :
```bash
python main.py
```

## Tests

Lancer les tests unitaires :
```bash
python -m unittest test_unitaire.py
python -m unittest test_password.py
```

## Structure du Projet

- `main.py` : Interface utilisateur principale
- `password_checker.py` : Module de vérification des mots de passe
- `password_generator.py` : Génération de mots de passe aléatoires
- `passphrase_generator.py` : Génération de passphrase avec la méthode EFF
- `test_unitaire.py` : Tests unitaires généraux
- `test_password.py` : Tests spécifiques des mots de passe
- `eff_large_wordlist.txt` : Liste de mots pour la génération de passphrase

## Auteur
Ronel BANKOLE
