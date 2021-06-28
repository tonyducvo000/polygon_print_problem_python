length_of_side = int(input("Enter the length of the side: "))
height = (2*length_of_side) - 1
number_of_space = length_of_side - 1

#for rows first half
for row_index in range(0, length_of_side, 1):
    #for index in (0, length, 1):
    for star_index in range( 0, number_of_space, 1):
        print(" ",end=' ')

    for x_index in range(0, length_of_side, 1):
        print("*", end=' ')
    length_of_side += 2

    for star_index in range( 0, number_of_space, 1):
        print(" ",end=' ')
    number_of_space -= 1
    print("")

length_of_side -= 4

#for row of bottom half
for row_index in range(row_index, 0, -1):
    for star_index in range(number_of_space, 0, 1):
        print(" ", end=' ')

    for x_index in range(0, length_of_side, 1):
        print("*", end=' ')
    length_of_side -= 2

    for star_index in range(number_of_space, 0, 1):
        print(" ", end=' ')
    number_of_space -= 1

    print("")







