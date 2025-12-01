import caeser_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
again = True

print(caeser_cipher_art.logo)


def caesar(user_text, user_shift, user_direction):
    end_text = ""
    if user_direction == 'decode':
        user_shift *= -1
    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + user_shift
            if new_position > len(alphabet):
                new_position %= len(alphabet)
                end_text += alphabet[new_position]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {user_direction}d text is {end_text}")

def encrypt(plain_text, shift_amount):
    encrypted_word = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > len(alphabet):
                new_position %= len(alphabet)
                encrypted_word += alphabet[new_position]
            else:
                encrypted_word += alphabet[new_position]
        else:
            encrypted_word += letter
    print(f"The encoded text is {encrypted_word}")

def decrypt(cipher_text, shift_amount):
    decrypted_word = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            if new_position > len(alphabet):
                new_position %= len(alphabet)
                decrypted_word += alphabet[new_position]
            else:
                decrypted_word += alphabet[new_position]
        else:
            decrypted_word += letter
    print(f"The decoded text is {decrypted_word}")

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(user_text=text, user_shift=shift, user_direction=direction)
    ask_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if ask_again == 'no':
        print("Goodbye :)")
        again = False
