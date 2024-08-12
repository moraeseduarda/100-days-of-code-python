# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
# Opens names file
with open("./Input/Names/invited_names.txt") as names_file:
    # Read each line/name
    names = names_file.readlines()

# Open starting letter file
with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    # Read starting text
    starting_text = starting_letter_file.read()
    for name in names:
        # Remove spaces at the beginning and at the end of the string
        new_name = name.strip()
        # Replaces placeholder to name
        new_letter = starting_text.replace(PLACEHOLDER, new_name)
        # Creates a new file
        # Note: "w" - this mode will create a file if the specified file does not exist
        new_file = open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w")
        # Writes the letter in the file
        new_file.write(new_letter)
