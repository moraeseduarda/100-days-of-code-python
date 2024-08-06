piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")


# Reverse the list
print(piano_keys[::-1])

# Items after index one and before index six
print(piano_keys[2:5])

# All items after index 1
print(piano_keys[2:])

# All items after index 1 and before index six but incremented by 2 ("jumping" two each time)
print(piano_keys[2:5:2])

# Every item "jumping" 3 each time
print(piano_keys[::3])

# All items after index zero
print(piano_tuple[1:])

# All items before index 4
print(piano_tuple[:4])
