#!/usr/bin/env python
import unittest
from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordChecker()
        
    def test_entropy_calculation(self):
        # Test avec différents types de mots de passe
        self.assertGreater(self.checker.calculate_entropy("abc123"), 0)
        self.assertEqual(self.checker.calculate_entropy(""), 0)
        self.assertGreater(self.checker.calculate_entropy("ABCdef123!@#"), 
                          self.checker.calculate_entropy("abcdef"))
    
    def test_password_strength(self):
        # Test des différents niveaux de force
        self.assertEqual(self.checker.check_password_strength("abc"), "Faible")
        self.assertIn(self.checker.check_password_strength("ABCdef123!@#"), 
                     ["Fort", "Très fort"])

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()
        
    def test_password_length(self):
        # Test des longueurs de mot de passe
        password = self.generator.generate_password(2, 2, 2, 2)
        self.assertEqual(len(password), 8)
        
    def test_password_composition(self):
        # Test de la composition du mot de passe
        password = self.generator.generate_password(1, 1, 1, 1)
        self.assertEqual(len(password), 4)
        
        # Vérifie qu'il y a au moins une lettre minuscule
        self.assertTrue(any(c.islower() for c in password))
        # Vérifie qu'il y a au moins une lettre majuscule
        self.assertTrue(any(c.isupper() for c in password))
        # Vérifie qu'il y a au moins un chiffre
        self.assertTrue(any(c.isdigit() for c in password))
        # Vérifie qu'il y a au moins un caractère spécial
        self.assertTrue(any(not c.isalnum() for c in password))

class TestPassphraseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PassphraseGenerator()
        
    def test_passphrase_words(self):
        # Test du nombre de mots dans la passphrase
        passphrase = self.generator.generate_passphrase(5)
        self.assertEqual(len(passphrase.split()), 5)
        
    def test_roll_dice(self):
        # Test de la fonction de lancer de dés
        dice_roll = self.generator.roll_dice(5)
        self.assertEqual(len(dice_roll), 5)
        self.assertTrue(all(c in '123456' for c in dice_roll))

if __name__ == '__main__':
    unittest.main()