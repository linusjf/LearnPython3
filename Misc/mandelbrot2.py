#!/usr/bin/env python
# Python code for Mandelbrot Fractal
# Import necessary libraries

from PIL import Image
from numpy import array
import colorsys

# setting the width of the output image as 1024

WIDTH = 1024
# a function to return a tuple of colors
# as integer value of rgb


def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(255 / i, 1.0, 0.5))
    return tuple(color.astype(int))


# function defining a mandelbrot


def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return (0, 0, 0)


# creating the new image in RGB mode

img = Image.new("RGB", (WIDTH, int(WIDTH / 2)))

pixels = img.load()

for x in range(img.size[0]):
    # displaying the progress as percentage
    pct = x / WIDTH
    print(f"{pct:%}\r", end="")
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot(
            (x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4)
        )
print(f"{1.0:%}")
# to display the created fractal after
# completing the given number of iterations
img.show()
img.save("mb.png")
