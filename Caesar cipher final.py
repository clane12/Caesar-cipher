# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game = True
# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, choose):
    original_text = original_text.lower()
    original_text = list(original_text)
    if choose == "encode":
        encrypted_code = ""
        for letter in original_text:
            if letter in alphabet:
                new = alphabet.index(letter)
                new += shift_amount
                if new == 26:
                    new = 0
                elif new >= 27:
                    new -= len(alphabet)
                encrypted_code += alphabet[new]
            else:
                encrypted_code += letter
        print(f"encrypted text is: {encrypted_code}")


    elif choose == "decode":
        decrypted_text = ""
        for letter in original_text:
            if letter in alphabet:
                new1 = alphabet.index(letter)
                new1 -= shift_amount
                if new1 <= -1:
                    new1 = len(alphabet) + new1
                decrypted_text += alphabet[new1]
            else:
                decrypted_text += letter
        print(f"decrypted text is: {decrypted_text}")


    else:
        print("you typed something wrong")


# TODO-3: Can you figure out a way to restart the cipher program?

while game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(original_text=text, shift_amount=shift, choose=direction)

    play = input("want to play another game yes or no:\n")
    if play == "yes":
        game = True
    elif play == "no":
        game = False
        print("Goodbye")
    else:
        print("You typed something else, Goodbye")
        break



