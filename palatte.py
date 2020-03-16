from PIL import Image

NUMBER_OF_CELLS = 10
NUMBER_OF_ROWS = 26

def get_colour_palatte():
    colour_palatte = Image.open("palatte.png")

    width = colour_palatte.size[0]
    height = colour_palatte.size[1]

    width_of_cells = int(width / NUMBER_OF_CELLS)
    height_of_cells = int(height / NUMBER_OF_ROWS)

    width_mid_point = int(width_of_cells / 2)
    height_mid_point = int(height_of_cells / 2)

    colours = []

    pixels = list(colour_palatte.getdata())

    for rows in range(NUMBER_OF_ROWS):
        for cells in range(NUMBER_OF_CELLS):
            root_offset_width = (cells * width_of_cells) + width_mid_point
            root_offset_height = (rows * height_of_cells) + height_mid_point
            index = root_offset_width + (root_offset_height * width)

            pixel = pixels[index]
            # print(index, root_offset_width, root_offset_height, pixel)
            colours.append(pixel)

    return colours