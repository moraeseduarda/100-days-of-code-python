# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += character
    print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

while end_program != True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    start_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower
    if start_again == "no":
        end_program = True
        print("Goodbye")