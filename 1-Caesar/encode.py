from helpers.inputs import input_int, input_text_strict
from helpers.outputs import print_substitution
from .utils import *

shift = input_int(max=26)
plaintext = input_text_strict()

sub_table = caesar_sub_table(shift)
ciphertext = caesar_encode(sub_table, plaintext)
print_substitution(plaintext, sub_table, ciphertext)