import numpy as np
import random
from lib.access_to_hues import access_to_hues
from lib.make_pixels_data_frame import make_pixels_data_frame


def convert_image_to_music(source,
                           scale_frequencies=(220.00, 246.94, 261.63, 293.66,
                                              329.63,
                                              349.23, 415.30),
                           sample_rate=22050, time_in_seconds=0.1,
                           number_pixels=60,
                           use_octaves=True,
                           random_pixels=False,
                           harmonies='U0'):
    hues = access_to_hues(source, random_pixels, number_pixels)

    pixels_data_frame, frequencies = make_pixels_data_frame(hues,
                                                            scale_frequencies)

    harmony = np.array([])
    harmony_value = _harmony_select[harmonies]

    song = np.array([])
    octaves = np.array([0.5, 1, 2])
    space = np.linspace(0, time_in_seconds, int(time_in_seconds * sample_rate),
                        endpoint=False)

    for pixel in range(number_pixels):
        if use_octaves:
            octave = random.choice(octaves)
        else:
            octave = 1

        if not random_pixels:
            value = octave * frequencies[pixel]
        else:
            value = octave * random.choice(frequencies)

        note = 0.5 * np.sin(2 * np.pi * value * space)
        harmony_note = 0.5 * np.sin(2 * np.pi * harmony_value * value * space)

        song = np.concatenate([song, note])
        harmony = np.concatenate([harmony, harmony_note])

    return song, pixels_data_frame, harmony


_harmony_select = {'U0': 1,
                   'ST': 16 / 15,
                   'M2': 9 / 8,
                   'm3': 6 / 5,
                   'M3': 5 / 4,
                   'P4': 4 / 3,
                   'DT': 45 / 32,
                   'P5': 3 / 2,
                   'm6': 8 / 5,
                   'M6': 5 / 3,
                   'm7': 9 / 5,
                   'M7': 15 / 8,
                   'O8': 2
                   }
