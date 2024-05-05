from helpers.tables import get_alphabet

def caesar_sub_table(shift):
    alphabet = get_alphabet()
    sub_table = {}
    for letter in alphabet:
        sub_letter = chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
        sub_table[letter] = sub_letter
    return sub_table


def caesar_encode(sub_table, plaintext):
    ciphertext = ""
    for plain_letter in plaintext:
        cipher_letter = sub_table[plain_letter]
        ciphertext += cipher_letter
    
    return ciphertext