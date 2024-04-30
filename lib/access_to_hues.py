import cv2
import random


def access_to_hues(source, random_pixels, number_pixels):
    hsv = cv2.cvtColor(source, cv2.COLOR_RGB2HSV)

    height, width, depth = source.shape

    i = 0
    j = 0

    hues = []
    if not random_pixels:
        for _ in range(number_pixels):
            hue = abs(hsv[i][j][0])
            hues.append(hue)
            i += 1
            j += 1
    else:
        for _ in range(number_pixels):
            i = random.randint(0, height - 1)
            j = random.randint(0, width - 1)
            hue = abs(hsv[i][j][0])
            hues.append(hue)

    return hues
