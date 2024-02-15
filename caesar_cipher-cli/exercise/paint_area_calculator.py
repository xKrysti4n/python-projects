from math import ceil
def paint_calc(height,width,coverage):
    num_cans = ceil((height * width) / coverage)
    print(f"You'll need {num_cans} cans of paint")



test_h = int(input("Height: "))
test_w = int(input("Width: "))
coverage = 5
paint_calc(test_h, test_w, coverage)