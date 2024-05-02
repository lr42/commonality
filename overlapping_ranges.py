# The first element of a range is inclusive, while the second element of a range is exclusive.  To get the size of the range, simply subtract the first value from the second.

#x = [ [5,7], [9,10], [12,15],  [20,24], [30,40],   [45,47]]
#y = [[3,                  16], [20, 26],   [36,43]        ]

x = [[5,7], [9,10], [12,15], [20,24], [30,40], [45,47]]
y = [[3,16],                 [20,26], [36,43]]

x_index = -1
y_index = -1

x_is_in_a_range = False
y_is_in_a_range = False

current_position = 0

final_position = 50

while x_index != len(x) and y_index != len(y):
    print(f"x_index: {x_index}   y_index: {y_index}")

    if x_is_in_a_range:
        next_x = x[x_index][1]
    elif x_index == len(x) - 1:
        next_x = final_position
    else:
        next_x = x[x_index+1][0]

    if y_is_in_a_range:
        next_y = y[y_index][1]
    elif y_index == len(y) - 1:
        next_y = final_position
    else:
        next_y = y[y_index+1][0]

    print(f"next_x: {next_x}   next_y: {next_y}")

    next_position = min(next_x, next_y)

    print(f"{current_position}-{next_position}: ", end="")
    if x_is_in_a_range and y_is_in_a_range:
        print(f"Both")
    elif x_is_in_a_range and not y_is_in_a_range:
        print(f"Only x")
    elif not x_is_in_a_range and y_is_in_a_range:
        print(f"Only y")
    else:
        print(f"Neither")

    if next_x == next_position:
        x_is_in_a_range = not x_is_in_a_range
        if x_is_in_a_range:
            x_index += 1
        print("switching x")

    if next_y == next_position:
        y_is_in_a_range = not y_is_in_a_range
        if y_is_in_a_range:
            y_index += 1
        print("switching y")

    current_position = next_position

    print()

