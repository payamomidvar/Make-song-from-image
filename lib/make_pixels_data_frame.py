import pandas as pd
import librosa
from lib.convert_hue_to_frequency import convert_hue_to_frequency


def make_pixels_data_frame(hues, scale_frequencies):
    pixels_data_frame = pd.DataFrame(hues, columns=['hues'])
    pixels_data_frame['frequencies'] = pixels_data_frame.apply(
        lambda row: convert_hue_to_frequency(row['hues'], scale_frequencies),
        axis=1)
    frequencies = pixels_data_frame['frequencies'].to_numpy()

    pixels_data_frame['notes'] = pixels_data_frame.apply(
        lambda row: librosa.hz_to_note(row['frequencies']), axis=1)

    pixels_data_frame['midi_number'] = pixels_data_frame.apply(
        lambda row: librosa.note_to_midi(row['notes']), axis=1)

    return pixels_data_frame, frequencies
