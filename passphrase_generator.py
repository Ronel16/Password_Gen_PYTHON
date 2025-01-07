#!/usr/bin/env python
import random

class PassphraseGenerator:
    def __init__(self):
        self.word_list = self._load_wordlist()
        
    def _load_wordlist(self):
        """
        Charge la liste de mots pour la méthode des dés
        À implémenter: charger depuis un fichier wordlist.txt
        """
        try:
            with open('wordlist.txt', 'r', encoding='utf-8') as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            # Liste de secours si le fichier n'est pas trouvé
            print("Attention: fichier wordlist.txt non trouvé, utilisation d'une liste de secours")
            return ["mot1", "mot2", "mot3", "mot4", "mot5"]
        
    def roll_dice(self, num_dice=5):
        """Simule un lancer de dés"""
        return ''.join(str(random.randint(1, 6)) for _ in range(num_dice))
        
    def generate_passphrase(self, num_words=5):
        """Génère une passphrase avec la méthode des dés"""
        passphrase = []
        for _ in range(num_words):
            # Sélection aléatoire d'un mot de la liste
            word = random.choice(self.word_list)
            passphrase.append(word)
        return ' '.join(passphrase)