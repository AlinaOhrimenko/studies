import random
import string

def make_inc_key(list):
    random_alf=list.copy()
    random.shuffle(random_alf)
    enc_key = dict(zip(list, random_alf))
    return enc_key
    
def compute_dec_key(enc_key):
    dec_key = {}
    for key, value in enc_key.items():
        dec_key[value] = key
    return dec_key

def encrypt_text(t, enc_key):
    enc_text = ""
    for char in t:
        if char in enc_key:
         enc_text += enc_key[char]
        else:
            enc_text += char
    print("your encrypted text is: ", enc_text)
    return enc_text

def decrypt_text(t, dec_key):
    dec_text=""
    for char in t:
        if char in dec_key:
         dec_text += dec_key[char]
        else:
            dec_text += char
    print("your decrypted text is: " ,dec_text)
    return dec_text

def test_all(t, list):
    inc_key=make_inc_key(list)
    dec_key=compute_dec_key(inc_key)
    enc_text=encrypt_text(t, inc_key)
    decrypt_text(enc_text, dec_key)

alfabet=list(string.ascii_lowercase)
plain_text=input("Please type the text you want to encrypt: ")
test_all(plain_text, alfabet)