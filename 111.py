#The re function is used to import characters outside the range of the ASCII table
#The string function is used to import all available characters from the ASCII table
#The random function is used to import a random set of integers for the changing key after every encrypt cycle is complete
#The deque function is used to add or remove elements from either ends of a list, it is used to help create the matrix for the Vigenere matrix

import re
import string
import random
from collections import deque


# This segment is for the removal of unnecessary characters from the imported list
all_char = list(string.printable)
to_be_removed = ['\t', '\n', '\r', '\x0b', '\x0c']
for i in to_be_removed:
    all_char.remove(i)

#Creates the Vigenere matrix used in the eccryption
#The rotate function is used to remove a character from one end and place it in the other end thus encrypting the plain text
all_char = deque(all_char)
vigenere_matrix = []
for i in range(len(all_char)):
    vigenere_matrix.append(list(all_char))
    all_char.rotate(-1)
vigenere_matrix = (vigenere_matrix)
all_char = list(all_char)

def encrypt_vigenere(plain_text,vigenere_matrix):
    key = ""
    cipher_text = ""

#This creates a random key for the encryption
    for i in range(len(plain_text)):
        key += random.choice(all_char)

#This encrypts the plain text using the random key generated
#The for function uses len in order to measure how many characters will be encrypted
#The X and Y variables are used to identify the positions for each letter of the plain text and the key
#The index function uses their locations as numbers and stores them
    for i in range(len(plain_text)):
        x = vigenere_matrix[0].index(plain_text[i])
        y = vigenere_matrix[0].index(key[i])
        cipher_text += vigenere_matrix[y][x]
    
    return cipher_text,key

#This decrypts the encrypted text and turns it back into plain text. This part is used to check and make sure that both texts match after the encryption
#The current_row variable contains the index of the plain text and the key
#The current_letter_index
def decrypt_vigenere(cipher_text,viginere_matrix,key):
    plain_text = ""
    for i in range(len(cipher_text)):
        current_row = vigenere_matrix[0].index(key[i])
        current_letter_index = vigenere_matrix[current_row].index(cipher_text[i])
        plain_text += vigenere_matrix[0][current_letter_index]
    return plain_text

#This part is used for the user to input the plain text that he wants encrypted
plain_text = input(("enter the text you want to encrypt:"))
bob = encrypt_vigenere(plain_text, vigenere_matrix)
print("the encrypted text:",bob[0])
print("the key:",bob[1])
print("the decrypt:",decrypt_vigenere(bob[0],vigenere_matrix,bob[1]))


file = open("Encrypt.txt",'w')
file.write("Encrypted message is:"+ bob[0])

file = open("Decrypt.txt",'w')
file.write("The decrypted  message is:"+plain_text)

file = open("Encrypt.txt",'w')
file.write("Encrypted message is:"+bob[1])