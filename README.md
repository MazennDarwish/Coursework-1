# How to run the code
. Click the run button

.Enter the desired text to be encrypted (this can consist of any letter, number or special character found on the keyboard)

.Once entered the program will encrypt the text and output the encryption, the key used and the decrypt which should match the orginal text

.The encrypt and decrypt will both be improted to an external .txt file known as encrypt.txt and decrypt.txt

# Vigenere Cypher

The Cypher chosen for the task is the Vigerne cypher. This file is created as a guide for the user and a quick introduction to the Vigenere matrix. The way the Vigenere cypher works is by creating
a matrix that contains all the characters that will be used in the encrypt/decrypt operation.

Once all the characters are placed, the user will be asked to input a word or phrase that he wants to be encrypted. It can consist of any letter, number or character from the standard keyboard.
The encryption method itself works by measuring the length of the phrase that the user has entered, and then generating a key depending on the length of the user input text. It then takes the first letter
and matches it to the first letter of the generated key. It then uses the index of each one in the generated matrix and finds the corrosponding letters that will be used to encrypt those sets of letters. The process is then
repeated for each letter of the word until all have been encrypted. The process is then repeated but in reveres in order to decrypt the word and check back that the decrypt matches the
orginal text. If both are a match then the proccess was successful.


![App Screenshot](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table.jpg)
