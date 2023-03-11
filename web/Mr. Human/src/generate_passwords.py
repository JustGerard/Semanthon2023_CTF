import string

file = open("passwords.txt", "w")

# PASSWORD = "Y0U RuN 1N70 k3Rn3L P4N1c"
START = "2W_TwP_3P92_m5Tp5N_R6P3e0"
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

file.write(START + "\n")


def shift(text: str) -> str:
    text = list(text)

    for index, character in enumerate(text):
        if character not in characters:
            continue
        old_index = characters.index(character)
        new_index = (old_index + 2) % len(characters)
        text[index] = characters[new_index]

    text.append(text.pop(0))

    return "".join(text)


output = START
for x in range(0, 774):
    output = shift(output)
    file.write(output + "\n")
print(output)
