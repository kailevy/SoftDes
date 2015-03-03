""" 
Kai Levy
SoftDes Spring 2015
Computational Art Project
"""

import random
from PIL import Image
import math as Math

func_list = [
    lambda a,b : a * b,                             # multiply
    lambda a,b : 0.5 * (a + b),                     # average 
    # lambda a,b : a ** 2 - b ** 2,                   # a**2 - b ** 2             (MUCH slower but kinda cool)
    # lambda a,b : Math.sqrt(abs(a**2 - b**2)),       # sqrt a ** 2 - b ** 2    (kinda cool)
    # lambda a : Math.exp(a / 2) - 1,                 # e ** (a / 2) - 1        (kinda cool)
    # lambda a: Math.tan(a / 2),                      # tan of a / 2            (kinda cool)
    # lambda a : a ** 2,                              # squared
    lambda a : Math.cos(a * Math.pi),               # cos_pi
    lambda a : Math.sin(a * Math.pi)                # sin_pi
    ]

FLEN = len(func_list)
FTWO = 2

def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    # TODO: implement this
    # if max_depth < 1 or (min_depth < 1 and random.randint(0,1)):
    #     return [random.randint(FLEN, FLEN + 2)]
    # else:
    #     index = random.randint(0,FLEN - 1)
    #     if index < FTWO:
    #         return [index, build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]
    #     else:
    #         return [index, build_random_function(min_depth - 1, max_depth - 1)]
    if max_depth < 1 or (min_depth < 1 and random.randint(0,1)):
        return random.choice([(lambda x,y,t: x), (lambda x,y,t: y), (lambda x,y,t: x * y * t)])
    else:
        index = random.randint(0,3)
        f1 = build_random_function(min_depth - 1, max_depth - 1)  
        if index == 0: 
            f2 = build_random_function(min_depth - 1, max_depth - 1)
            return lambda x,y,t: f1(x,y,t) * f2(x,y,t)
        elif index == 1:
            f2 = build_random_function(min_depth - 1, max_depth - 1)
            return lambda x,y,t: 0.5 * (f1(x,y,t) + f2(x,y,t))
        elif index == 2:
            return lambda x,y,t: Math.cos(f1(x,y,t) * Math.pi)
        else: 
            return lambda x,y,t: Math.sin(f1(x,y,t) * Math.pi)
    # else:
    #     index = random.randint(0,3)
    #     f1 = build_random_function(min_depth - 1, max_depth - 1)  
    #     if index < FTWO: 
    #         f2 = build_random_function(min_depth - 1, max_depth - 1)
    #         return func_list[index](f1(x,y),f2(x,y))
    #     else:
    #         return func_list[index](f1(x,y))


def evaluate_random_function(f, x, y, t):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["FLEN"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["FLEN + 1"],0.1,0.02)
        0.02
    """
    # TODO: implement this

    if f[0] == FLEN:
        return x
    elif f[0] == FLEN + 1:
        return y - t
    elif f[0] == FLEN + 2:
        return t
    if f[0] < FTWO:
        return func_list[f[0]](evaluate_random_function(f[1],x,y,t),evaluate_random_function(f[2],x,y,t))
    else:
        return func_list[f[0]](evaluate_random_function(f[1],x,y,t))



def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
        >>> remap_interval(20, 0, 200, -1, 1)
        -0.8
    """
    # TODO: implement this
    return (output_interval_start + float((val - input_interval_start)) / 
        (input_interval_end - input_interval_start) * (output_interval_end - 
            output_interval_start))


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, frames, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7,9)
    green_function = build_random_function(7,9)
    blue_function = build_random_function(7,9)

    for k in range(frames):
        t = remap_interval(k, 0, frames, -1, 1)
        # Create image and loop over all pixels
        im = Image.new("RGB", (x_size, y_size))
        pixels = im.load()
        for i in range(x_size):
            for j in range(y_size):
                x = remap_interval(i, 0, x_size, -1, 1)
                y = remap_interval(j, 0, y_size, -1, 1)
                pixels[i, j] = (
                        # color_map(evaluate_random_function(red_function, x, y, t)),
                        # color_map(evaluate_random_function(green_function, x, y, t)),
                        # color_map(evaluate_random_function(blue_function, x, y, t))
                        color_map(red_function(x,y,t)),
                        color_map(green_function(x,y,t)),
                        color_map(blue_function(x,y,t))
                        )

        im.save(filename + '_' + str(k) + '.png')



if __name__ == '__main__':
    generate_art("vis/art", 150)