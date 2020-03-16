from PIL import Image
from colored import fg, bg, attr
from math import sqrt

from palatte import get_colour_palatte

from os import get_terminal_size

ts = get_terminal_size()

map = Image.open("map2.png")

map_resized = map.resize((ts.columns, ts.lines -1))
pixels = list(map_resized.getdata())

COLOURS = get_colour_palatte()
colour_ledger = {}

def pixel_average(pixel):
    r, g, b, g = pixel

    # total = r
    # total += (g << 8)
    # total += (b << 16)

    return ((r + g + b) / 3)

def present(index):
    if index >= len(pixels):
        return False

    pixel = pixels[index]
    if (pixel is None):
        return False
    
    return (pixel_average(pixel) < 245)

def closest_color(rgb):
    ledger = colour_ledger.get(rgb)
    if ledger is not None:
        return ledger

    r, g, b, g = rgb
    color_diffs = []
    for color in COLOURS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    closet =  min(color_diffs)[1]

    colour_ledger[rgb] = closet

    return closet

def what_char(index):
    diff_between_lines = ts.columns

    char = ' '

    if (present(index)):

        colour = closest_color(pixels[index])
        fg_colour = fg(COLOURS.index(colour))

        top = present(index - diff_between_lines)
        # top_left = present(top - 1)
        # top_right = present(top + 1)

        left = present(index - 1)
        right = present(index + 1)

        bottom = present(index + diff_between_lines)
        # bottom_left = bottom - 1
        # bottom_right = bottom + 1
    
        if (top and bottom and left and right):
            char = '+'
        elif (top and bottom and not left and not right):
            char = '|'
        elif (top and bottom and not left and right):
            char = '|'
        elif (top and bottom and left and not right):
            char = '|'
        elif (top and not bottom and left and right):
            char = '-'
        elif (not top and bottom and left and right):
            char = '-'
        elif (not top and not bottom and left and right):
            char = '−'
        elif (not top and bottom and not left and not right):
            char = '⊤'
        elif (top and not bottom and not left and not right):
            char = '⊥'
        elif (not top and not bottom and left and not right):
            char = '⊣'
        elif (not top and not bottom and not left and right):
            char = '⊢'
        elif (top and not bottom and not left and right):
            char = '\\'
        elif (not top and bottom and left and not right):
            char = '\\'
        elif (not top and bottom and not left and right):
            char = '/'
        elif (top and not bottom and left and not right):
            char = '/'
        else:
            char = '*'

        char = "%s%s%s" % (fg_colour, char, attr(0))

    return char

for index in range((ts.columns * ts.lines)):
    print(what_char(index), end="")

