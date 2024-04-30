import streamlit as st
from widgets.select_box import SelectBox
from lib.subjects import Subjects
from widgets.select_image import select_image
from lib.music_parameters import MusicParameters
from lib.settings_parameters import SettingsParameters
from lib.scale_parameters import ScaleParameters
from lib.song import Song
from widgets.audio import Audio


def run():
    st.title("Making Music From Images")

    st.markdown(
        "This little app converts an image into a song."
        " Play around with the various inputs belows using different images!")

    image_to_load = select_image()
    scale_column, key_column, octave_column, harmony_column = st.columns(4)

    with scale_column:
        scale = SelectBox(title='What scale would you like to use?',
                          subject=Subjects.Scales).select_options()

    with key_column:
        key = SelectBox(title='What key would you like to use?',
                        subject=Subjects.Keys).select_options()

    with octave_column:
        octave = SelectBox(title='What octave would you like to use?',
                           subject=Subjects.Octaves).select_options()

    with harmony_column:
        harmonies = SelectBox(title='What harmony would you like to use?',
                              subject=Subjects.Harmonies).select_options()

    random_pixels_column, use_octaves_column = st.columns(2)
    with random_pixels_column:
        random_pixels = st.checkbox('Use random pixels to build song?',
                                    value=True)
    with use_octaves_column:
        use_octaves = st.checkbox('Randomize note octaves while building song?',
                                  value=True)

    duration_column, number_pixels_column = st.columns(2)
    with duration_column:
        time_in_seconds = st.slider('Note duration [s]', min_value=0.01,
                                    max_value=1.0,
                                    step=0.01, value=0.2)

    with number_pixels_column:
        number_pixels = st.slider(
            'How many pixels to use? (More pixels take longer)',
            min_value=12, max_value=320, step=1, value=60)

    st.markdown("## Settings")
    rate_hz_chorus_column, delay_seconds_column, distortion_column, gain_column = st.columns(4)

    with rate_hz_chorus_column:
        chorus = st.slider('Rate HZ chorus', min_value=0.0,
                           max_value=100.0,
                           step=0.1, value=0.0)

    with delay_seconds_column:
        delay_seconds = st.slider('Delay seconds', min_value=0.0, max_value=2.0,
                                  step=0.1, value=0.0)

    with distortion_column:
        distortion = st.slider('Distortion', min_value=0.0, max_value=100.0,
                               step=1.0,
                               value=0.0)

    with gain_column:
        gain = st.slider('Gain', min_value=0.0, max_value=100.0, step=1.0,
                         value=0.0)

    size_column, wet_level_column, dry_level_column, width_column = st.columns(
        4)
    with size_column:
        size = st.slider('Size', min_value=0.0, max_value=1.0,
                         step=0.1,
                         value=0.0)

    with wet_level_column:
        wet_level = st.slider('Wet level', min_value=0.0, max_value=1.0,
                              step=0.1,
                              value=0.0)
    with dry_level_column:
        dry_level = st.slider('Dry level', min_value=0.1, max_value=1.0,
                              step=0.1,
                              value=0.1)
    with width_column:
        width = st.slider('Width', min_value=0.0, max_value=1.0, step=0.1,
                          value=0.0)

    cutoff_hz_column, resonance_column, drive_column = st.columns(3)
    with cutoff_hz_column:
        cutoff_hz = st.slider('Cutoff HZ', min_value=0.0, max_value=1000.0,
                              step=1.0, value=0.0)
    with resonance_column:
        resonance = st.slider('Resonance', min_value=0.0, max_value=1.0,
                              step=0.1, value=0.0)
    with drive_column:
        drive = st.slider('Drive', min_value=1.0, max_value=100.0, step=0.1,
                          value=1.0)

    rate_hz_phaser_column, depth_column, semitones_column = st.columns(3)
    with rate_hz_phaser_column:
        rate_hz_phaser = st.slider('Rate HZ phaser', min_value=0.0,
                                   max_value=100.0,
                                   step=0.1, value=0.0)

    with depth_column:
        depth_phaser = st.slider('Depth', min_value=0.0, max_value=1.0,
                                 step=0.1,
                                 value=0.0)

    with semitones_column:
        semitones = st.slider('Semitones', min_value=0.0, max_value=12.0,
                              step=1.0, value=0.0)

    scale_parameters = ScaleParameters(octave, key, scale)

    music_parameters = MusicParameters(image_to_load,
                                       time_in_seconds, random_pixels,
                                       use_octaves,
                                       number_pixels, harmonies, )
    settings_parameters = SettingsParameters(gain, distortion, cutoff_hz,
                                             resonance, drive, delay_seconds,
                                             size, wet_level, dry_level, width,
                                             rate_hz_phaser, depth_phaser,
                                             semitones, chorus, )
    song = Song(music_parameters, settings_parameters, scale_parameters)
    song.run(lambda audio_bytes, song_data_frame: Audio(audio_bytes,
                                                        song_data_frame).run())
