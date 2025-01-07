#!/usr/bin/env python
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation
        
    def generate_password(self, length_lower=0, length_upper=0, length_digits=0, length_special=0):
        """Génère un mot de passe aléatoire selon les critères spécifiés"""
        password = []
        
        # Générer chaque type de caractère selon les longueurs demandées
        password.extend(random.choice(self.lowercase) for _ in range(length_lower))
        password.extend(random.choice(self.uppercase) for _ in range(length_upper))
        password.extend(random.choice(self.digits) for _ in range(length_digits))
        password.extend(random.choice(self.special_chars) for _ in range(length_special))
        
        # Mélanger le mot de passe
        random.shuffle(password)
        return ''.join(password)