#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Invert RGB colors | ----\n", fg("red")))

# user interaction
rgb_color = tuple([int(i) for i in input("RGB color (seperated with commas): ").split(", ")])

# variables
highest_RGB = 255

# function
def invert(rgb_tuple):
    inverted_rgb = []
    # invert rgb colors
    for number in rgb_tuple:
        inverted_rgb.append(highest_RGB - number)

    return tuple(inverted_rgb)

inverted_rgb_color = stylize(invert(rgb_color), fg("red"))
print(f"\nThis RGB color {rgb_color} is inverted\nthis RGB color {inverted_rgb_color}.\n")
