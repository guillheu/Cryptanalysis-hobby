The Caesar cipher is a simple substitution cipher where the whole alphabet is shifted a given amount of positions. This gives us a substitution table that we can use to encode the plaintext.

Decoding the plaintext can be done simply by reversing the shift in the substitution table, and running the ciphertext through the encoder with the reverse substitution table.

Encoding example:

Input text:
```
This is the story of a man named Stanley.
```

Plaintext:
```
THISISTHESTORYOFAMANNAMEDSTANLEY
```

Shift: 3

Substitution table:
| Plain Alphabet | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|----------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher Alphabet| D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

Ciphertext:
```
QEFPFPQEBPQLOVLCXJXKKXJBAPQXKIBV
```


Decoding example:

Decoding example:
```
DELYWPJHZCVPOQZCLNZXALYJHTESLMTRMFTWOTYRHSPCPSPHLDPXAWZJPPYFXMPCQZFCEHZDPGPY
```

Shift: 15

Substitution table:
| Plain Alphabet | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|----------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher Alphabet| P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |

Plaintext:
```
STANLEYWORKEDFORACOMPANYWITHABIGBUILDINGWHEREHEWASEMPLOYEENUMBERFOURTWOSEVEN
```