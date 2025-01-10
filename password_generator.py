#!/usr/bin/env python
"""
Ce module implémente un générateur de mots de passe aléatoires.
Il permet de créer des mots de passe complexes en spécifiant le nombre
de chaque type de caractère souhaité.

"""

import random

class PasswordGenerator:
    def __init__(self):
        # Types de caractères disponibles
        self.minuscules = list('abcdefghijklmnopqrstuvwxyz')
        self.majuscules = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.chiffres = list('0123456789')
        self.speciaux = list('!@#$%^&*()_+-=[]{}|;:,.<>?')
        
    def generer_password(self, length_lower=0, length_upper=0, length_digits=0, length_special=0):
        """Génère un mot de passe avec les critères demandés"""
        password = []
        
        # Ajout des caractères demandés
        password.extend(random.choice(self.minuscules) for _ in range(length_lower))
        password.extend(random.choice(self.majuscules) for _ in range(length_upper))
        password.extend(random.choice(self.chiffres) for _ in range(length_digits))
        password.extend(random.choice(self.speciaux) for _ in range(length_special))
        
        # Mélange pour plus de sécurité
        random.shuffle(password)
        return ''.join(password)