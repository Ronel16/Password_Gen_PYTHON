# Générateur et Testeur de Mot de Passe

Ce projet est un outil de sécurité permettant de générer et tester des mots de passe selon les critères de l'ANSSI.

## Fonctionnalités

- Test de force de mot de passe basé sur l'entropie
- Génération de mot de passe aléatoire avec critères personnalisables
- Génération de passphrase selon la méthode des dés
- Interface en ligne de commande interactive

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Ronel16/Password_Gen_PYTHON
cd Password_Gen_PYTHON
```

2. (Optionnel) Créez et activez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix
venv\Scripts\activate     # Sur Windows
```

## Utilisation

Lancez le programme principal :
```bash
python main.py
```

## Tests

Pour lancer les tests unitaires :
```bash
python -m unittest test_password.py
```

## Structure du Projet

- `main.py` : Point d'entrée du programme
- `password_checker.py` : Module de vérification de force de mot de passe
- `password_generator.py` : Générateur de mot de passe aléatoire
- `passphrase_generator.py` : Générateur de passphrase
- `test_password.py` : Tests unitaires
- `wordlist.txt` : Liste de mots pour la génération de passphrase (à fournir)

## Critères de l'ANSSI

Le programme suit les recommandations de l'ANSSI pour le calcul de l'entropie des mots de passe :
- Moins de 64 bits : Faible
- Entre 64 et 80 bits : Moyen
- Entre 80 et 100 bits : Fort
- Plus de 100 bits : Très fort
