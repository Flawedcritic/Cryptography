import string

# The dictionary and list are both used in dec_convert function
letters = string.ascii_uppercase
alpha_dict = {letter: index for index, letter in enumerate(letters)}
alpha_list = list(letters)

# List of most common English words and letter combinations, Used for analyzing decrypted text , Sorted by frequency of occurrence
most_common = [
    "E", "T", "A", "O", "T", "N", "S", "R", "H", "L", "TH", "HE", "IN", "ER", "AN", "RE", "ON", "AT", "EN", "ND",
    "TI", "ES", "OR", "TE", "OF", "ST", "TO", "ED", "IS", "IT", "AL", "AR", "NT", "AS", "HA", "SE", "ME", "HI",
    "VE", "OF", "WE", "NG", "EA", "OM", "UR", "OW", "MA", "UT", "SO", "ET", "EE", "RS", "NO", "LL", "BE", "OU",
    "LD", "WA", "EA", "LY", "THE", "AND", "ING", "ION", "ENT", "HER", "FOR", "THA", "ERE", "HAT", "HIS", "TER",
    "WAS", "YOU", "ITH", "VER", "ALL", "WIT", "THI", "TIO", "ATI", "HIN", "OUR", "ECT", "ONE", "TIS", "ARE",
    "IVE", "CON", "RES", "ONS", "PRO", "WHI", "AVE", "EVE", "NCE", "EST", "INT", "STA", "NOT", "IST", "EAR",
    "ITE", "LEA", "ITI", "SIO", "MEN", "UND", "ING", "ALL", "ERE", "HER", "HIS", "TIC", "TIO", "IRE", "ORS",
    "ORT", "OST", "EVE", "OVE", "UND", "UNT", "IST", "IGH", "EAR", "EAK", "EAL", "ESS", "INK", "ORE", "TION",
    "THAT", "THER", "WITH", "TING", "HERE", "IONS", "MENT", "THEY", "OULD", "HAVE", "WITI", "FROM", "HICH",
    "THIS", "WHER", "WHIC", "TION", "EVER", "OUGH", "IGHT", "WERE", "WHEN", "STHE", "THES", "INTE", "EDTH",
    "ATIO", "NGTH", "ALLY", "NTHE", "ERED", "SAND", "NDTH", "ATING", "ANDT", "SING", "FROM", "INGT", "THER",
    "MENT", "HEST", "THEM", "THEN", "NTHE", "WHIC", "TING", "THER", "TAIN", "MENT", "VENT", "OMEN", "INGE",
    "ATED", "OUND", "ANCE", "RITY", "TION", "STLE", "DEST", "AINS", "INGS"
]

# Decrypts the given Cipher text by trying different keys and finding the most probable answer
def affine_decrypt():
    # Possible keys for decryption
    possible_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    sent = input("What text do you want to decrypt?: ")  # Get text to decrypt
    actual_sent = sent.upper()  # Convert text to uppercase
    changed_sent_dict = {}  # Dictionary to store decrypted text with corresponding keys
    for a in possible_keys:
        for b in range(0, 26):
            changed_sent = ''  # Initialize decrypted text
            for i in actual_sent:
                if i not in alpha_list and i != " ":
                    changed_sent = changed_sent  # Skip non-alphabetic characters
                elif i == ' ':
                    changed_sent = changed_sent + ' '  # Preserve spaces
                else:
                    changed_sent = changed_sent + dec_convert(i, a, b)  # Decrypt each letter
            key = changed_sent  # Use the decrypted text as the key for the dictionary
            value = [a, b]  # Store 'a' and 'b' values in a list
            changed_sent_dict[key] = value  # Assign the list [a, b] as the value for the key 'changed_sent'
    show_answers(changed_sent_dict)  # Show the most probable answers

# Returns decrypted values to affine_decrypt
def dec_convert(letter, key1, key2):
    a = pow(key1, -1, 26)  # Find modular multiplicative inverse
    c = ((alpha_dict[letter] - key2) * a) % 26  # Decryption formula
    m = alpha_list[c]  # Get decrypted letter
    return m  # Return decrypted letter

# Show the most probable answers
def show_answers(a):
    changed_sent_dict = list(a.keys())  # Get the decrypted texts
    frequency = {}
    for i in changed_sent_dict:
        for m in most_common:
            if m in i:
                frequency[i] = frequency.get(i, 0) + 1  # Count occurrences of common English words and letter combinations
            else:
                frequency[i] = frequency.get(i, 0)

    # Sort the decrypted texts by frequency of occurrence of common English words and letter combinations
    sorted_frequency = dict(sorted(frequency.items(), key=lambda key_val: key_val[1], reverse=True))
    first10 = list(sorted_frequency.items())[:11]  # Get the top 10 most probable answers
    print("Most likely answers are:")
    for key, value in first10:
        print(f"if the keys are {a[key]} then the value is {key} {value}")  # Print the most probable answers
    gotit = input("Is your answer in this list? (1 = yes, 2 = no, any other button = quit)")
    if gotit == "1":
        print("Quitting")  # If user finds their answer in the top 10 list, print 'Quitting'
    elif gotit == "2":
        therest = list(sorted_frequency.items())[11:]  # Get the rest of the decrypted texts
        for key, value in therest:
            print(f"if the keys are {a[key]} then the value is {key} {value}")  # Print the rest of the decrypted texts
    else:
        print("quitting!")  # Quit if user inputs anything other than '1' or '2'

def main():
    affine_decrypt()

if __name__ == "__main__":
    main()  # Execute main function only if the script is run directly