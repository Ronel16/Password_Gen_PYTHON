#!/usr/bin/env python
"""
Programme principal intégrant toutes les fonctionnalités
"""

from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def main():
    # Initialisation
    checker = PasswordChecker()
    generator = PasswordGenerator()
    passphrase_gen = PassphraseGenerator()
    
    while True:
        print("\n🔐 Menu Principal")
        print("1. 🔍 Tester un mot de passe")
        print("2. 🎲 Générer un mot de passe")
        print("3. 📝 Générer une passphrase")
        print("4. 👋 Quitter")
        
        choice = input("\nChoix (1-4): ")
        
        if choice == "1":
            # Test de mot de passe
            password = input("Mot de passe à tester: ")
            entropy = checker.calculate_entropy(password)
            strength = checker.check_password_strength(password)
            print(f"Entropie: {entropy:.2f} bits")
            print(f"Force: {strength}")
            
        elif choice == "2":
            try:
                # Génération de mot de passe
                print("\nComposition du mot de passe:")
                lower = int(input("Minuscules: "))
                upper = int(input("Majuscules: "))
                digits = int(input("Chiffres: "))
                special = int(input("Caractères spéciaux: "))
                
                if lower < 0 or upper < 0 or digits < 0 or special < 0:
                    raise ValueError("Nombres négatifs non autorisés")
                
                password = generator.generate_password(lower, upper, digits, special)
                entropy = checker.calculate_entropy(password)
                strength = checker.check_password_strength(password)
                
                print(f"\nMot de passe: {password}")
                print(f"Entropie: {entropy:.2f} bits")
                print(f"Force: {strength}")
                
            except ValueError as e:
                print(f"Erreur: {str(e)}")
            
        elif choice == "3":
            try:
                # Génération de passphrase
                num_words = int(input("Nombre de mots (défaut: 5): ") or "5")
                if num_words <= 0:
                    raise ValueError("Le nombre doit être positif")
                
                passphrase = passphrase_gen.generate_passphrase(num_words)
                print(f"\nPassphrase: {passphrase}")
                entropy = checker.calculate_entropy(passphrase.replace(" ", ""))
                strength = checker.check_password_strength(passphrase.replace(" ", ""))
                print(f"Entropie: {entropy:.2f} bits")
                print(f"Force: {strength}")
                
            except ValueError as e:
                print(f"Erreur: {str(e)}")
            
        elif choice == "4":
            print("Au revoir!")
            break
        else:
            print("Option invalide")

if __name__ == "__main__":
    main()