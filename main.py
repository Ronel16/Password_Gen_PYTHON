#!/usr/bin/env python
from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def main():
    checker = PasswordChecker()
    generator = PasswordGenerator()
    passphrase_gen = PassphraseGenerator()
    
    while True:
        print("\nGénérateur et testeur de mot de passe")
        print("1. Tester un mot de passe")
        print("2. Générer un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")
        
        choice = input("\nChoisissez une option (1-4): ")
        
        if choice == "1":
            password = input("Entrez le mot de passe à tester: ")
            entropy = checker.calculate_entropy(password)
            strength = checker.check_password_strength(password)
            print(f"Entropie: {entropy:.2f} bits")
            print(f"Force: {strength}")
            
        elif choice == "2":
            try:
                lower = int(input("Nombre de minuscules: "))
                upper = int(input("Nombre de majuscules: "))
                digits = int(input("Nombre de chiffres: "))
                special = int(input("Nombre de caractères spéciaux: "))
                
                if lower < 0 or upper < 0 or digits < 0 or special < 0:
                    raise ValueError("Les longueurs doivent être positives")
                
                password = generator.generate_password(lower, upper, digits, special)
                entropy = checker.calculate_entropy(password)
                strength = checker.check_password_strength(password)
                
                print(f"\nMot de passe généré: {password}")
                print(f"Entropie: {entropy:.2f} bits")
                print(f"Force: {strength}")
            except ValueError as e:
                print(f"Erreur: {str(e)}")
            
        elif choice == "3":
            try:
                num_words = int(input("Nombre de mots pour la passphrase (défaut: 5): ") or "5")
                if num_words <= 0:
                    raise ValueError("Le nombre de mots doit être positif")
                
                passphrase = passphrase_gen.generate_passphrase(num_words)
                print(f"\nPassphrase générée: {passphrase}")
                
                # Afficher aussi l'entropie de la passphrase
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
            print("Option invalide, veuillez réessayer")

if __name__ == "__main__":
    main()