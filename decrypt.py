alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'

plaintext = ''

for char in ciphertext:
    if char in alphabet:
        char_index = key.index(char)
        decrypted_text = alphabet[char_index]
        plaintext += decrypted_text
        
    else:
        plaintext += char
        
print(plaintext)
        
