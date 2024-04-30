import numpy as np
from lib.scale_parameters import ScaleParameters


class Scale:
    _scale = {
        'AEOLIAN': [0, 2, 3, 5, 7, 8, 10],
        'BLUES': [0, 2, 3, 4, 5, 7, 9, 10, 11],
        'PHYRIGIAN': [0, 1, 3, 5, 7, 8, 10],
        'CHROMATIC': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        'DORIAN': [0, 2, 3, 5, 7, 9, 10],
        'HARMONIC_MINOR': [0, 2, 3, 5, 7, 8, 11],
        'LYDIAN': [0, 2, 4, 6, 7, 9, 11],
        'MAJOR': [0, 2, 4, 5, 7, 9, 11],
        'MELODIC_MINOR': [0, 2, 3, 5, 7, 8, 9, 10, 11],
        'MINOR': [0, 2, 3, 5, 7, 8, 10],
        'MIXOLYDIAN': [0, 2, 4, 5, 7, 9, 10],
        'NATURAL_MINOR': [0, 2, 3, 5, 7, 8, 10],
        'PENTATONIC': [0, 2, 4, 7, 9],
    }

    def __init__(self, scale_parameters: ScaleParameters):
        self.parameters = scale_parameters

    def make(self):
        note_frequencies = self._get_piano_notes()

        scale_intervals = ['A', 'a', 'B', 'C', 'c', 'D', 'd', 'E', 'F', 'f',
                           'G',
                           'g']

        index = scale_intervals.index(self.parameters.key)

        new_scale = scale_intervals[index:12] + scale_intervals[:index]

        scale = self._scale[self.parameters.scale]
        frequencies = []
        for i in range(len(scale)):
            note = new_scale[scale[i]] + str(self.parameters.octave)
            frequency = note_frequencies[note]
            frequencies.append(frequency)
        return frequencies

    def _get_piano_notes(self):
        self.octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a',
                       'B']
        base_frequency = 440
        keys = np.array([x + str(y) for y in range(0, 9) for x in self.octave])

        self.start = np.where(keys == 'A0')[0][0]
        self.end = np.where(keys == 'C8')[0][0]
        keys = keys[self.start:self.end + 1]

        note_frequencies = dict(
            zip(keys, [2 ** ((n + 1 - 49) / 12) * base_frequency for n in
                       range(len(keys))]))
        note_frequencies[''] = 0.0
        return note_frequencies
