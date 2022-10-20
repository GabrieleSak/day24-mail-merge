PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        letter_with_name = letter.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as new_file:
            new_file.write(letter_with_name)
