"""Tests unitaires du projet"""
import unittest
from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

class TestPassword(unittest.TestCase):
    def setUp(self):
        """Initialisation des objets pour les tests"""
        self.checker = PasswordChecker()
        self.generator = PasswordGenerator()
        self.passphrase = PassphraseGenerator()

    def test_verifier_caracteres(self):
        """Test du vérificateur de caractères"""
        # Test avec un mot de passe complexe
        min, maj, chif, spe = self.checker.verifier_caracteres("Test123!")
        self.assertEqual(min, 3)  # "est"
        self.assertEqual(maj, 1)  # "T"
        self.assertEqual(chif, 3)  # "123"
        self.assertEqual(spe, 1)  # "!"
        
    def test_generer_password(self):
        """Test du générateur de mot de passe"""
        password = self.generator.generer_password(2, 2, 2, 2)
        self.assertEqual(len(password), 8)
        
        # Test de la composition
        min, maj, chif, spe = self.checker.verifier_caracteres(password)
        self.assertEqual(min, 2)
        self.assertEqual(maj, 2)
        self.assertEqual(chif, 2)
        self.assertEqual(spe, 2)

    def test_passphrase_generator(self):
        """Test du générateur de passphrase"""
        # Test du lancer de dés
        resultat = self.passphrase.lancer_des()
        self.assertEqual(len(resultat), 5)
        for chiffre in resultat:
            self.assertTrue(int(chiffre) >= 1 and int(chiffre) <= 6)

        # Test de la génération de passphrase
        passphrase = self.passphrase.generer_passphrase(5)
        mots = passphrase.split()
        self.assertEqual(len(mots), 5)
        
    def test_force_password(self):
        """Test de l'évaluation de force"""
        # Mot de passe très faible
        self.assertEqual(self.checker.evaluer_force("abc"), "❌ Très faible")
        
        # Mot de passe fort
        self.assertEqual(self.checker.evaluer_force("Test123!@#"), "💪 Fort")

if __name__ == '__main__':
    unittest.main()