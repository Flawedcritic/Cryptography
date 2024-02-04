# Importing necessary libraries
import math
import string
import sys

#The dictionary and list are both used in enc_convert() and dec_convert functions
alpha_dict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S': 18, 'T' : 19, 'U': 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
alpha_list = list(string.ascii_uppercase)
#This list is used in affine_encrypt() and affine_decrypt() functions
spec_chara = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

#This function prompts the user for what they want to do(encrypt? or decrypt?)
def enc_or_dec():
    #if correct input is put in, the while loop terminates, otherwise it will loop again
    while True:
        print("Enter 1 for encryption, 2 for decryption, q to quit\n")
        try:
            #s is the input the user puts in
            s = input("What would you like to do: ")
            #breaks while loop when correct input is given and raises Value error when incorrect value is given
            if s == '1' or s == '2' or s == 'q':
                break
            else:
                raise ValueError
        except ValueError:
            print("\n")
            print("Incorrect input, please input correct value\n")
        #allows Ctrl+C to be used to interrupt the program
        except KeyboardInterrupt:
            print("\n")
            sys.exit('Interrupted\n')
    #returns s to main function
    return s

#Gets keys from the user
def get_keys():
    while True:
        try:
            print("\n")
            print("Enter Ctrl+C to quit")
            print("The first key must be a coprime of 26\n")
            key1 = int(input("Enter first key: "))
            key2 = int(input("Enter second key: "))

            while True:

                if key1 < 0:
                    key1 += 26
                else:
                    break

            if math.gcd(key1, 26) == 1:
                break
            else:
                print("not a coprime")
        except KeyboardInterrupt:
            print("\n")
            sys.exit("Interrupted")
        except ValueError:
            print("Not a number")
        

    return key1, key2

#returns encrypted values to affine_encrypt
def enc_convert(letter, key1, key2):
    m = (key1 * alpha_dict[letter] + key2) % 26
    c = alpha_list[m]
    return c

#Encrypts the given Cipher text by sending each letter to the enc_convert function
def affine_encrypt():
    key1, key2 = get_keys() 
    sent = input("What text do you want to encrypt?: ")
    actual_sent = sent.upper()
    changed_sent = ''
    for i in actual_sent:
        if i.isnumeric() == True:
            changed_sent = changed_sent
        elif i in spec_chara:
            changed_sent = changed_sent
        elif i == ' ':
            changed_sent = changed_sent + ' '
        else:
            changed_sent = changed_sent + enc_convert(i, key1, key2)
    return changed_sent

#returns multiplicative inverse of given key
def find_inverse(key):
    possible_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for i in possible_keys:
        if (key*i) % 26 == 1:
            inverse = i
            break
    return inverse

#returns decrypted values to affine_decrypt
def dec_convert(letter, key1, key2):
    a = find_inverse(key1)
    c = ((alpha_dict[letter] - key2) * a) % 26
    m = alpha_list[c]
    return m

#Decrypts the given Cipher text by sending each letter to the dec_convert function
def affine_decrypt():
    key1, key2 = get_keys()
    sent = input("What text do you want to decrypt?: ")
    actual_sent = sent.upper()
    changed_sent = ''
    for i in actual_sent:
        if i.isnumeric == True:
            pass
        elif i in spec_chara:
            pass
        elif i == ' ':
            changed_sent = changed_sent + ' '
        else:
            changed_sent = changed_sent + dec_convert(i, key1, key2)
    return changed_sent

#Main function
def main():
    a = enc_or_dec()
    if a == '1':
        value = affine_encrypt()
        print(value)
    elif a == '2':
        value = affine_decrypt()
        print(value)
    elif a == 'q':
        print("quitting!")
        exit
        
#prevents the main function from being called when this python file is called somewhere else
if __name__ == "__main__":
    main()