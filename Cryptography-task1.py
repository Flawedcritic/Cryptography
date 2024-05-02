# Importing necessary libraries
import math 
import string  
import sys 

# The dictionary and list are both used in enc_convert() and dec_convert functions
letters = string.ascii_uppercase  # Get all uppercase letters
alpha_dict = {letter: index for index, letter in enumerate(letters)}  # Dictionary mapping letters to their index
alpha_list = list(letters)  # List of uppercase letters

# This function prompts the user for what they want to do (encrypt? or decrypt?)
def enc_or_dec():
    # Loop until correct input is provided
    while True:
        print("Enter 1 for encryption, 2 for decryption, q to quit\n")
        try:
            s = input("What would you like to do: ")  # Get user input
            if s == '1' or s == '2' or s == 'q':  # Check if input is valid
                break  
            else:
                raise ValueError  # Raise ValueError for incorrect input
        except ValueError:
            print("\n")
            print("Incorrect input, please input correct value\n")
        except KeyboardInterrupt:
            print("\n")
            sys.exit('Interrupted\n')  # Handle interrupt (Ctrl+C)

    return s  # Return user's choice

# Gets keys from the user
def get_keys():
    while True:
        try:
            print("\n")
            print("Enter Ctrl+C to quit")
            print("The first key must be a coprime of 26\n")
            key1 = int(input("Enter first key: "))  
            key2 = int(input("Enter second key: ")) 

            while True:
                # Ensure key1 is positive
                if key1 < 0:
                    key1 += 26
                else:
                    break

            if math.gcd(key1, 26) == 1:  # Check if key1 is coprime with 26
                break
            else:
                print("not a coprime")
        except KeyboardInterrupt:
            print("\n")
            sys.exit("Interrupted")  # Handle interrupt (Ctrl+C)
        except ValueError:
            print("Not a number")  # Handle non-numeric input

    return key1, key2  # Return the keys

# Returns encrypted values to affine_encrypt
def enc_convert(letter, key1, key2):
    m = (key1 * alpha_dict[letter] + key2) % 26  # Encryption formula
    c = alpha_list[m]  # Get encrypted letter
    return c  # Return encrypted letter

# Encrypts the given Cipher text by sending each letter to the enc_convert function
def affine_encrypt():
    key1, key2 = get_keys()  # Get encryption keys
    sent = input("What text do you want to encrypt?: ")  
    actual_sent = sent.upper() 
    changed_sent = ''  # Initialize encrypted text
    for i in actual_sent:
        if i.isnumeric() == True:
            changed_sent = changed_sent
        elif i not in alpha_list and i != " ":
            changed_sent = changed_sent
        elif i == ' ':
            changed_sent = changed_sent + ' '
        else:
            changed_sent = changed_sent + enc_convert(i, key1, key2)  # Encrypt each letter
    return changed_sent  # Return encrypted text

# Returns decrypted values to affine_decrypt
def dec_convert(letter, key1, key2):
    a = pow(key1, -1, 26)  # Find modular multiplicative inverse
    c = ((alpha_dict[letter] - key2) * a) % 26  # Decryption formula
    m = alpha_list[c]  # Get decrypted letter
    return m  # Return decrypted letter

# Decrypts the given Cipher text by sending each letter to the dec_convert function
def affine_decrypt():
    key1, key2 = get_keys()  # Get decryption keys
    sent = input("What text do you want to decrypt?: ")
    actual_sent = sent.upper() 
    changed_sent = ''  # Initialize decrypted text
    for i in actual_sent:
        if i.isnumeric == True:
            changed_sent = changed_sent
        elif i not in alpha_list and i != " ":
            changed_sent = changed_sent
        elif i == ' ':
            changed_sent = changed_sent + ' '
        else:
            changed_sent = changed_sent + dec_convert(i, key1, key2)  # Decrypt each letter
    return changed_sent  # Return decrypted text

# Main function, Get user's choice (encrypt or decrypt), Encrypt if user chooses 1, Decrypt if user chooses 2, Quit if user chooses q
def main():
    a = enc_or_dec() 
    if a == '1':
        value = affine_encrypt()  
        print(value)  # Print encrypted text
    elif a == '2':
        value = affine_decrypt()  
        print(value)  # Print decrypted text
    elif a == 'q':
        print("quitting") 
        exit  # Exit the program

# Prevents the main function from being called when this python file is called somewhere else
if __name__ == "__main__":
    main()