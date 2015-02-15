""" 
Kai Levy
SoftDes Spring 2015
Computational Art Project
"""

import random
from PIL import Image
import math as Math
import cProfile



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
    # func_list = [['prod',['a'],['b']],['avg',['a'],['b']]]
    func_list = [['prod',['a'],['b']],['avg',['a'],['b']],['cos_pi',['a']],['sin_pi',['a']]]
    my_func = random.choice(func_list)
    if min_depth < 1 or (max_depth < 1 and random.randint(0,1)):
        return random.choice(['x','y'])
    else:
        for i in range(len(my_func)):
            if type(my_func[i]) is list:
                my_func[i] = build_random_function(min_depth - 1, max_depth - 1)
        return my_func

def choose_x(a,b):
    return a

def choose_y(a,b):
    return b

def multiply(a,b):
    return a * b

def average(a,b):
    return 0.5 * (a + b)

def cos_pix(a,b):
    return Math.cos(a * Math.pi)

def sin_pix(a,b):
    return Math.sin(a * Math.pi)

funcDict = {'x': choose_x, 'y': choose_y, 'prod': multiply, 'avg': average, 'cos_pi': cos_pix, 'sin_pi': sin_pix}  

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    # TODO: implement this
    
    # def choose_x(a,b):
    #     return a

    # def choose_y(a,b):
    #     return b

    # def multiply(a,b):
    #     return a * b

    # def average(a,b):
    #     return 0.5 * (a + b)

    # def cos_pix(a,b):
    #     return Math.cos(a * Math.pi)

    # def sin_pix(a,b):
    #     return Math.sin(a * Math.pi)

    lenF = len(f)
    # funcDict = {'x': choose_x, 'y': choose_y, 'prod': multiply, 'avg': average, 'cos_pi': cos_pix, 'sin_pi': sin_pix}
    if lenF == 1:
        return funcDict[f[0]](x,y)
    elif lenF == 2:
        return funcDict[f[0]](evaluate_random_function(f[1],x,y),0)
    else:
        return funcDict[f[0]](evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))



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
    return output_interval_start + float((val - input_interval_start)) / (input_interval_end - input_interval_start) * (output_interval_end - output_interval_start)


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


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7,9)
    green_function = build_random_function(7,9)
    blue_function = build_random_function(7,9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    cProfile.run('generate_art("myart_4.png")')
    # generate_art("myart_4.png")
    # print evaluate_random_function(build_random_function(7,10),0.4,0.2)
    # print build_random_function(7,9)
    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    # test_image("noise.png")