# Instructions
# This is a difficult challenge. 💪

# You are going to write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:
# Image 1

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.
# Image 2

# So an input of A3 should place an X at the position shown below:
# Image 3

# First, your program must take the user input and convert it to a usable format.

# Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Hints
# See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

# Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

# list = [['A', 'B, 'C'], 'E', 'F', 'G']
# E is list[1] C is list[0][2]

# Check your formatting. This is correctly formatted:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# vs.

# Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️','X ' , '⬜️']

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Pega a letra A e coloca em minúscula
letter = position[0].lower()
# Cria uma lista para ajudar a indexação
abc = ["a", "b", "c"]
# Encontra o índice da letra na lista (esse é o índice que indica a posição do X dentro da lista)
index_letter = abc.index(letter)

# Pega o número, transforma o número em int, subtrai 1 para encontrar o índice que indica a lista
index_number = int(position[1]) - 1

# De fora (index_number) para dentro (index_letter)
map[index_number][index_letter] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")