import cv2
from PIL import Image
import streamlit as st
from lib.music_parameters import MusicParameters
from lib.settings_parameters import SettingsParameters
from lib.scale_parameters import ScaleParameters
from lib.scale import Scale
from lib.convert_image_to_music import convert_image_to_music
from scipy.io import wavfile
from pedalboard.io import AudioFile
from numpy import vstack, float32
from pedalboard import Pedalboard, Chorus, Reverb, Gain, LadderFilter, Phaser, \
    Delay, PitchShift, Distortion


class Song:
    def __init__(self, music_parameters: MusicParameters,
                 settings_parameters: SettingsParameters,
                 scale_parameters: ScaleParameters, ):
        self.music_parameters = music_parameters
        self.settings_parameters = settings_parameters
        self.scale_parameters = scale_parameters

    def run(self, call_back_function):
        if self.music_parameters.image_to_load is not None:
            image = self._preparing_images_for_music()
            scale = Scale(self.scale_parameters).make()
            song, song_data_frame, harmony = \
                convert_image_to_music(image,
                                       scale_frequencies=scale,
                                       time_in_seconds=self.music_parameters.time_in_seconds,
                                       random_pixels=self.music_parameters.random_pixels,
                                       use_octaves=self.music_parameters.use_octaves,
                                       number_pixels=self.music_parameters.number_pixels,
                                       harmonies=self.music_parameters.harmonies)
            audio_bytes = self._make_audio_bytes(song, harmony)
            call_back_function(audio_bytes, song_data_frame)
        else:
            st.write("Waiting for an image to be uploaded...")

    def _preparing_images_for_music(self):
        image = Image.open(self.music_parameters.image_to_load)
        extension = image.format
        image.save(f"img.{extension}")
        image = cv2.imread(f"img.{extension}")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def _make_audio_bytes(self, song, harmony):
        song_combined = vstack((song, harmony))
        wavfile.write('song.wav', rate=22050,
                      data=song_combined.T.astype(float32))
        open('song.wav', 'rb')
        with AudioFile('song.wav', 'r') as file:
            audio = file.read(file.frames)
            sample_rate = file.samplerate

        board = Pedalboard([
            Gain(gain_db=self.settings_parameters.gain),
            Distortion(drive_db=self.settings_parameters.distortion),
            LadderFilter(mode=LadderFilter.Mode.HPF12,
                         cutoff_hz=self.settings_parameters.cutoff_hz,
                         resonance=self.settings_parameters.resonance,
                         drive=self.settings_parameters.drive),
            Delay(delay_seconds=self.settings_parameters.delay_seconds),
            Reverb(room_size=self.settings_parameters.size,
                   wet_level=self.settings_parameters.wet_level,
                   dry_level=self.settings_parameters.dry_level,
                   width=self.settings_parameters.width),
            Phaser(rate_hz=self.settings_parameters.rate_hz_phaser,
                   depth=self.settings_parameters.depth_phaser),
            PitchShift(semitones=self.settings_parameters.semitones),
            Chorus(rate_hz=self.settings_parameters.chorus)
        ])
        effected = board(audio, sample_rate)
        with AudioFile('processed_song.wav', 'w', sample_rate,
                       effected.shape[0]) as file:
            file.write(effected)
        audio_file2 = open('processed_song.wav', 'rb')
        audio_bytes2 = audio_file2.read()

        return audio_bytes2
