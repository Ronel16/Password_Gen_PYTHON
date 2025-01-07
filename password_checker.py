#!/usr/bin/env python
import math
import string

class PasswordChecker:
    def __init__(self):
        self.lowercase = set(string.ascii_lowercase)
        self.uppercase = set(string.ascii_uppercase)
        self.digits = set(string.digits)
        self.special_chars = set(string.punctuation)
        
    def calculate_entropy(self, password):
        """Calcule l'entropie d'un mot de passe selon les critères de l'ANSSI"""
        char_space = 0
        
        if any(c in self.lowercase for c in password):
            char_space += 26
        if any(c in self.uppercase for c in password):
            char_space += 26
        if any(c in self.digits for c in password):
            char_space += 10
        if any(c in self.special_chars for c in password):
            char_space += len(self.special_chars)
            
        if char_space == 0:
            return 0
            
        entropy = len(password) * math.log2(char_space)
        return entropy
        
    def check_password_strength(self, password):
        """Évalue la force d'un mot de passe basé sur son entropie"""
        entropy = self.calculate_entropy(password)
        
        if entropy < 64:
            return "Faible"
        elif entropy < 80:
            return "Moyen"
        elif entropy < 100:
            return "Fort"
        else:
            return "Très fort"