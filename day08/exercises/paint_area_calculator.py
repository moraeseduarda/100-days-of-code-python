import math
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    round_up_num = math.ceil(number_of_cans)
    print(f"You'll need {round_up_num} cans of paint.")

test_h = int(input()) 
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
