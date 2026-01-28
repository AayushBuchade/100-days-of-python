import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# # def decrypt(original_text,shift_amount):
# #     cipher_text = ""
# #     for letter in original_text:
# #         shifted_position = alphabet.index(letter) - shift_amount
# #         shifted_position %= len(alphabet)
# #         cipher_text += alphabet[shifted_position]
# #     print(f"Here is the decoded result:{cipher_text}")



def caesar(original_text, shift_amount, encrypt_or_decrypt):
    text = ""
    if encrypt_or_decrypt == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabet:
            text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            text += alphabet[shifted_position]
    print(f"Here is the {encrypt_or_decrypt}d result : {text}")


should_continue = True

while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift,encrypt_or_decrypt=direction)

    restart_cipher =input("do you wanna restart ? type 'no' to stop \n").lower()
    if restart_cipher == "no":
        should_continue = False
        print("thanks !!!!!!!")