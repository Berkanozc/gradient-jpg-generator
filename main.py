from PIL import Image
import random
import numpy as np

MIN_RGB_VALUE = 0
MAX_RGB_VALUE = 255
OUT_PATH = "out"
FILE_TYPE = ".jpg"


def run():
    print('Welcome to the random gradient background generator')
    print('How many different gradients do you want to generate (round number): ')
    count = int(input())

    print('Give a width (round number): ')
    width = int(input())
    print('Give a height (round number): ')
    height = int(input())

    for x in range(count):
        array = get_gradient_3d(width, height, generate_random_color(), generate_random_color(), (True, False, False))
        Image.fromarray(np.uint8(array)).save(OUT_PATH + "/background-" + str(x) + FILE_TYPE)


def generate_random_color():
    return (
        random.randint(MIN_RGB_VALUE, MAX_RGB_VALUE),
        random.randint(MIN_RGB_VALUE, MAX_RGB_VALUE),
        random.randint(MIN_RGB_VALUE, MAX_RGB_VALUE)
    )


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=float)
    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result


run()

