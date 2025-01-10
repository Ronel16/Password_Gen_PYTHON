"""Programme principal - Générateur et testeur de mots de passe"""
from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def main():
    # Initialisation des classes
    checker = PasswordChecker()
    generator = PasswordGenerator()
    passphrase_gen = PassphraseGenerator()
    
    while True:
        print("\n🔐 Générateur et Testeur de mot de passe 🔐")
        print("1. 🔍 Tester un mot de passe")
        print("2. 🎲 Générer un mot de passe")
        print("3. 🎯 Générer une passphrase (méthode des dés)")
        print("4. 📖 Instructions méthode des dés")
        print("5. 👋 Quitter")
        
        choix = input("\nChoix (1-5): ")
        
        if choix == "1":
            try:
                password = input("Mot de passe à tester: ")
                force = checker.evaluer_force(password)
                print(f"\nForce: {force}")
                
                # Détails de la composition
                min, maj, chif, spe = checker.verifier_caracteres(password)
                print(f"\nDétails du mot de passe:")
                print(f"📍 Minuscules: {min}")
                print(f"📍 Majuscules: {maj}")
                print(f"📍 Chiffres: {chif}")
                print(f"📍 Spéciaux: {spe}")
                
            except Exception as e:
                print(f"❌ Erreur: {str(e)}")
                
        elif choix == "2":
            try:
                print("\nComposition du mot de passe:")
                nb_min = int(input("Minuscules: "))
                nb_maj = int(input("Majuscules: "))
                nb_chif = int(input("Chiffres: "))
                nb_spe = int(input("Caractères spéciaux: "))
                
                if min(nb_min, nb_maj, nb_chif, nb_spe) < 0:
                    raise ValueError("Les nombres doivent être positifs")
                
                password = generator.generer_password(nb_min, nb_maj, nb_chif, nb_spe)
                print(f"\n✨ Mot de passe généré: {password}")
                print(f"💪 Force: {checker.evaluer_force(password)}")
                
            except ValueError as e:
                print(f"❌ Erreur: {str(e)}")
                
        elif choix == "3":
            try:
                nb_mots = int(input("Nombre de mots (5 recommandé): "))
                if nb_mots <= 0:
                    raise ValueError("Le nombre de mots doit être positif")
                passphrase = passphrase_gen.generer_passphrase(nb_mots)
                print(f"\n✨ Passphrase générée: {passphrase}")
                # Analyse de la force
                force = checker.evaluer_force(passphrase.replace(" ", ""))
                print(f"💪 Force: {force}")
                
            except ValueError as e:
                print(f"❌ Erreur: {str(e)}")

        elif choix == "4":
            passphrase_gen.afficher_instructions()
                
        elif choix == "5":
            print("👋 Au revoir!")
            break
            
        else:
            print("❌ Option invalide")

if __name__ == "__main__":
    main()