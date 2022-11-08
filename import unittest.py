import unittest
from project_code import encrypt_vigenere
from project_code import decrypt_vigenere


class Test(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(encrypt_vigenere("Hello @ World", "{l\RPi6z~eFSx"), "Czb-.h`yUC'.K")

    def test_decryption(self):
        self.assertEqual(decrypt_vigenere("Czb-.h`yUC'.K", "{l\RPi6z~eFSx"), "Hello @ World")
        





if __name__ == '_main_':
    unittest.main()