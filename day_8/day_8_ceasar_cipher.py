alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_amount, choice):
    try:
        shift_amount = int(shift_amount)

        if shift_amount > 26:
            shift_amount = shift_amount % 26

        output_text = ""

        for letter in input_text:
            if letter in alphabet:
                position = alphabet.index(letter)

                if choice == 'encode':
                    new_position = position + shift_amount
                elif choice == 'decode':
                    new_position = position - shift_amount
                else:
                    break

                output_text += alphabet[new_position]
            else:
                output_text += letter

        if len(output_text) > 0:
            print(f"The {choice}d text is {output_text}")
        else:
            print('You have entered the wrong commant')

    except ValueError: 
        print('You have entered the wrong data')


run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")

    caesar(input_text=text, shift_amount=shift, choice=direction)

    is_run = input('Do you want to restart the program? Type "Yes" or "No"\n')

    if is_run.capitalize() == 'Yes':
        continue
    elif is_run.capitalize() == 'No':
        run = False
    else:
        print('You have entered the wrong command. Program is closed')
        run = False
