#----------------- CHALLENGE FOR FUTURE ----------------------
#    Attempt to allow spaces and punctuation so that a user 
# could write whole statements rather than just singular words

#Initialize the variables/intro string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print("\n\n" + logo)

def encode(input):
    "input is a str which you want to encode using caesar cipher"
    "output is the encoded phrase"

    lst_enc = [x for x in input]
    encoded_lst = []
    for x in lst_enc:
        enc_val = (int(alphabet.index(x))) + secret_value
        if enc_val > 25:
            enc_val = enc_val%26
        elif enc_val < -26:
            enc_val = enc_val%26
        else:
            pass
        encoded_lst.append(alphabet[enc_val])

    return ''.join(encoded_lst)

def decode(input):
    "input is a str which you want to decode using caesar cipher"
    "output is the original phrase"

    lst_dec = [x for x in input]
    decoded_lst = []
    for x in lst_dec:
        enc_val = (int(alphabet.index(x))) - secret_value
        if enc_val > 25:
            enc_val = enc_val%26
        elif enc_val < -26:
            enc_val = enc_val%26
        else:
            pass
        decoded_lst.append(alphabet[enc_val])

    return ''.join(decoded_lst)


play = input("\nWelcome to the Caesar Cipher!\nPress (E) for encode or (D) for decode:  ").lower()
secret_value = int(input("What value do you want to cipher by?  "))
if play == 'e':
    encode_phrase = (input("What phrase do you want to encode?  "))
    print(f"Your encoded phrase is:\n\n {encode(encode_phrase)}\n")
elif play == 'd':
    decode_phrase = (input("What phrase do you want to decode?  "))
    print(f"Your decoded phrase is:\n\n {decode(decode_phrase)}\n")




