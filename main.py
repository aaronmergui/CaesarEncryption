def encrypt(key, plaintext):
    """
    This function encrypts a plain text given a key, using the caesar encryption method.
    We need to use the ascii table to do so, that is why we are using the ord and chr method.
    ord is to have the value from the ascii table while chr gives a char from the ascii value.
    :param key: encryption key
    :param plaintext: plain text to encrypt
    :return: encrypted plaintext
    """

    result = ""

    for letter in plaintext:

        if not letter.isalpha():  # if the char in the plaintext is not a letter

            result += letter

        elif letter.islower():  # for lower letters the value of a is 97

            result += chr((ord(letter) - 97 + key) % 26 + 97)

        else:  # for upper letters the value of A is 65
            result += chr((ord(letter) - 65 + key) % 26 + 65)

    return result


def decrypt(key, plaintext):
    result = ""

    for letter in plaintext:

        if not letter.isalpha():

            result += letter

        elif letter.islower():  # for lower letters the value of a is 97

            result += chr((ord(letter) - 97 - key) % 26 + 97)

        else:  # for upper letters the value of A is 65
            result += chr((ord(letter) - 65 - key) % 26 + 65)

    return result


def brute_force_decrypt(encrypted_text):
    key = 1
    while key <= 26:
        print("Is the decrypted code is: \"" + decrypt(key, encrypted_text) + "\" ? \n"
                                                                              "Enter yes if it is the decrypted code, "
                                                                              "no otherwise.")
        user_input = input()

        if user_input == "yes":
            print("The caesar key was: " + str(key))
            return

        elif user_input != "no":
            print("Wrong answer ! ")

        else:
            key += 1

    print("We could not find the encrypted text")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(encrypt(1, "a2bA"))
    print(decrypt(1, encrypt(1, "a2bA")))

    brute_force_decrypt(encrypt(4, "My name is Aaron Mergui and I am learning python !"))
