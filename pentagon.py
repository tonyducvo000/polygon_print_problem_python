length_of_side = int(input("Enter the length of the side: "))

max_length = (length_of_side * 3) - 2
top_half_height = length_of_side - 1
bottom_half_height = length_of_side
row_index = 0

if length_of_side % 2 == 0:  # even
    isEven = True
    number_of_space = int((max_length - 2) / 2)
    number_of_stars = 2
    addTwo = True
    evenIteration = False
else:  # odd
    isEven = False
    number_of_space = int((max_length - 1) / 2)
    number_of_stars = 1
    addTwo = False
    evenIteration = True

# handle number of rows - TOP HALF
while (row_index < top_half_height):

    # handle left-side spacing
    for space_index in range(0, number_of_space, 1):
        print(" ", end=' ')
    space_index = 0

    # handle stars
    for star_index in range(0, number_of_stars, 1):
        print("*", end=' ')

    # handle right side spacing
    for space_index in range(0, number_of_space, 1):
        print(" ", end=' ')
    space_index = 0

    # updating variables

    if (evenIteration):
        number_of_space -= 2
    else:
        number_of_space -= 1

    evenIteration = not evenIteration

    if(addTwo):
        number_of_stars += 2
    else:
        number_of_stars += 4

    addTwo = not addTwo

    print("")

    row_index += 1

############################## BOTTOM HALF ###################################

for row_index in range(0, bottom_half_height, 1):
    for space_index in range(0, number_of_space, 1):
        print(" ", end=' ')

    for star_index in range(0, number_of_stars, 1):
        print("*", end=' ')

    for space_index in range(0, number_of_space, 1):
        print(" ", end=' ')

    number_of_space += 1
    number_of_stars -= 2

    print("")
