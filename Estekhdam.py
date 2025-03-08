from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode , original_text , shift_amount):

    output = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for word in original_text :
        if word not in alphabet:
            output += word

        else :
            output += alphabet[(alphabet.index(word) + shift_amount) % len(alphabet)]

    print(f"Here is the {direction}d result: {output}")

flag = True
while flag == True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction , text , shift)
    game_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if game_continue == "no":
        flag = False
        print("GoodBye!")
