from .utils import *
from helpers.inputs import input_int, input_text_strict
from helpers.tables import get_alphabet
from helpers.outputs import print_substitution


rshift = -input_int(max=26)
ciphertext = input_text_strict()

sub_table = caesar_sub_table(rshift)
plaintext = caesar_encode(sub_table, ciphertext)
print_substitution(plaintext, sub_table, ciphertext)