def paint_calc(height, width, cover):
    value = round((height * width) / cover)
    return value

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
cover = int(input("Coverage: "))
paint = paint_calc(test_h, test_w, cover)

print(f"You need {paint} paint buckets")