# Importing necessary libraries
import string

#The dictionary and list are both used in dec_convert function
alpha_dict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S': 18, 'T' : 19, 'U': 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
alpha_list = list(string.ascii_uppercase)
#This list is used inaffine_decrypt() 
spec_chara = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


#returns decrypted values to affine_decrypt
def dec_convert(letter, key1, key2):
    a = pow(key1,-1,26)
    c = ((alpha_dict[letter] - key2) * a) % 26
    m = alpha_list[c]
    return m

#Decrypts the given Cipher text by sending each letter to the dec_convert function
def affine_decrypt():
    possible_keys = [1,3,5,7,9,11,15,17,19,21,23,25]
    sent = input("What text do you want to decrypt?: ")
    actual_sent = sent.upper()
    for a in possible_keys:
        for b in range(0,26):
            changed_sent = ''
            for i in actual_sent:
                if i.isnumeric == True:
                    changed_sent = changed_sent
                elif i in spec_chara:
                    changed_sent = changed_sent
                elif i == ' ':
                    changed_sent = changed_sent + ' '
                else:
                    changed_sent = changed_sent + dec_convert(i, a, b)
            print(f"If a = {a} and b = {b}, the decrypted text is: {changed_sent}")

def main():
    affine_decrypt()

if __name__ == "__main__":
    main()
