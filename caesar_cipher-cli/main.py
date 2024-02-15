from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift, direction):
    end_text = ""
    if direction == "decode": 
        shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}\n")

print(logo)
want_continue = True

while want_continue:
    valid_answer = False
    while not valid_answer:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "decode" or direction == "encode" and not text.isnumeric():
            valid_answer = True
        else:
            print("Invalid answers")
    caesar(text, shift, direction)
    want_continue_input = input("Do you want to continue? (yes/no) \n").lower()
    if want_continue_input == "no":
        want_continue = False

print("Goodbye!")