#!/usr/bin/env python
"""
Ce module implémente un vérificateur de force de mot de passe basé sur les recommandations de l'ANSSI.
Il permet de calculer l'entropie d'un mot de passe et d'évaluer sa force.

"""

class PasswordChecker:
    def __init__(self):
        # Caractères possibles pour un mot de passe
        self.minuscules = 'abcdefghijklmnopqrstuvwxyz'
        self.majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.chiffres = '0123456789'
        self.speciaux = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    def verifier_caracteres(self, password):
        """Compte les différents types de caractères"""
        nb_minuscules = sum(1 for c in password if c in self.minuscules)
        nb_majuscules = sum(1 for c in password if c in self.majuscules)
        nb_chiffres = sum(1 for c in password if c in self.chiffres)
        nb_speciaux = sum(1 for c in password if c in self.speciaux)
        
        return (nb_minuscules, nb_majuscules, nb_chiffres, nb_speciaux)
    
    def evaluer_force(self, password):
        """Évalue la force d'un mot de passe"""
        # Critères de force
        score = 0
        
        # Longueur minimum
        if len(password) >= 8:
            score += 1
            
        # Présence des différents types
        mins, majs, chifs, specs = self.verifier_caracteres(password)
        if mins > 0: score += 1  # Minuscules
        if majs > 0: score += 1  # Majuscules
        if chifs > 0: score += 1  # Chiffres
        if specs > 0: score += 1  # Spéciaux
        
        # Retourne une évaluation basée sur le score
        if score < 2:
            return "❌ Très faible"
        elif score < 3:
            return "⚠️ Faible"
        elif score < 4:
            return "✅ Moyen"
        elif score < 5:
            return "💪 Fort"
        else:
            return "🔒 Très fort"