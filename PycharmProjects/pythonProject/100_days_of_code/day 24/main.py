PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completted_letter:
        completted_letter.write(new_letter)





# with open("./Input/Letters/starting_letter.txt") as letter:
#     letter_example = letter.read()
#
# with open("./Input/Names/invited_names.txt") as names:
#      list_of_names = names.readlines()
#
# for names in list_of_names:
#     name = names.replace("\n", "")
#     letter_name = letter_example.replace("[name]", name)
#     with open(f"./Output/ReadyToSend/letter_to_{name}", "w") as letter:
#         letter.write(letter_name)



