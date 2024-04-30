from enum import Enum


class Subjects(Enum):
    Scales = ['AEOLIAN', 'BLUES', 'PHYRIGIAN',
              'CHROMATIC', 'DORIAN', 'HARMONIC_MINOR',
              'LYDIAN', 'MAJOR', 'MELODIC_MINOR',
              'MINOR', 'MIXOLYDIAN', 'NATURAL_MINOR',
              'PENTATONIC']
    Keys = ['A', 'a', 'B', 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g']

    Octaves = [1, 2, 3]

    Harmonies = ['U0', 'ST', 'M2', 'm3', 'M3', 'P4', 'DT',
                 'P5', 'm6', 'M6', 'm7', 'M7', 'O8']
