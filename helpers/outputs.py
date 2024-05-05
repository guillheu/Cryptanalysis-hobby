from tabulate import tabulate

def print_table(table, headers='keys', tablefmt='grid'):
    print(tabulate(table, headers=headers, tablefmt=tablefmt))

def print_substitution(plaintext, sub_table, ciphertext):
    print("""
    #########################
    ####### Plaintext #######
    #########################
    """)
    print(plaintext)
    print("""
    ##########################
    ### Substitution table ###
    ##########################
    """)
    print_table(sub_table)
    print("""
    ##########################
    ####### Ciphertext #######
    ##########################
    """)
    print(ciphertext)
