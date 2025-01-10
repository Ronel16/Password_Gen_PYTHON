# Générateur de passphrase basé sur la méthode des dés de l'EFF
import random

class PassphraseGenerator:
    def __init__(self):
        # Dictionnaire qui stockera les mots
        self.wordlist = {}
        # Chargement de la liste depuis le fichier
        self.load_wordlist()

    def load_wordlist(self):
        """Charge la liste de mots du fichier"""
        try:
            # Lecture du fichier EFF
            with open('eff_large_wordlist.txt', 'r') as f:
                for line in f:
                    # Format: numéro mot
                    num, word = line.strip().split('\t')
                    self.wordlist[num] = word
        except FileNotFoundError:
            print("❌ Fichier eff_large_wordlist.txt non trouvé")
    
    def lancer_des(self):
        """Simule un lancer de 5 dés"""
        return ''.join(str(random.randint(1, 6)) for _ in range(5))
    
    def generer_passphrase(self, nb_mots=5):
        """Génère une passphrase avec le nombre de mots spécifié"""
        if len(self.wordlist) == 0:
            return "❌ Erreur: Liste de mots non chargée"
            
        mots = []
        for _ in range(nb_mots):
            while True:
                code = self.lancer_des()
                if code in self.wordlist:
                    mots.append(self.wordlist[code])
                    break
        return ' '.join(mots)

    def afficher_instructions(self):
        """Instructions pour générer une passphrase avec des dés physiques"""
        print("\n📌 Instructions pour la méthode des dés:")
        print("1. Lancez 5 dés")
        print("2. Notez les chiffres (ex: 1-4-2-6-3)")
        print("3. Cherchez le mot dans la liste EFF")
        print("4. Répétez pour obtenir plusieurs mots\n")
        