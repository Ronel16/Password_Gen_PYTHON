#!/usr/bin/env python
"""
Ce module implémente un générateur de mots de passe aléatoires.
Il permet de créer des mots de passe complexes en spécifiant le nombre
de chaque type de caractère souhaité.

"""

import random
import string

class PasswordGenerator:
    """
    Classe qui génère des mots de passe aléatoires avec des critères personnalisables.
    L'utilisateur peut spécifier le nombre exact de chaque type de caractère
    (minuscules, majuscules, chiffres, caractères spéciaux).
    """

    def __init__(self):
        """
        Initialise les ensembles de caractères disponibles pour la génération
        de mots de passe.
        """
        # Définition des différents types de caractères disponibles
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits              # 0-9
        self.special_chars = string.punctuation  # !@#$%^&*()...
        
    def generate_password(self, length_lower=0, length_upper=0, length_digits=0, length_special=0):
        """
        Génère un mot de passe aléatoire selon les critères spécifiés.
        
        Args:
            length_lower (int): Nombre de lettres minuscules souhaité
            length_upper (int): Nombre de lettres majuscules souhaité
            length_digits (int): Nombre de chiffres souhaité
            length_special (int): Nombre de caractères spéciaux souhaité
            
        Returns:
            str: Le mot de passe généré
            
        Note:
            Le mot de passe final est mélangé aléatoirement pour éviter
            que les caractères de même type soient groupés.
        """
        # Liste qui contiendra tous les caractères du mot de passe
        password = []
        
        # Génération des différents types de caractères selon les quantités demandées
        # On utilise des listes en compréhension pour plus d'efficacité
        password.extend(random.choice(self.lowercase) for _ in range(length_lower))
        password.extend(random.choice(self.uppercase) for _ in range(length_upper))
        password.extend(random.choice(self.digits) for _ in range(length_digits))
        password.extend(random.choice(self.special_chars) for _ in range(length_special))
        
        # Mélange aléatoire des caractères pour plus de sécurité
        random.shuffle(password)
        
        # Conversion de la liste de caractères en chaîne
        return ''.join(password)