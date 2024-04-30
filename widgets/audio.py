from streamlit import audio, download_button


class Audio:
    def __init__(self, audio_bytes, song_data_frame):
        self.audio_bytes = audio_bytes
        self.song_data_frame = song_data_frame

    def run(self):
        audio(self.audio_bytes, format='audio/wav')

        download_button('Download Song as CSV',
                        data=self.song_data_frame.to_csv().encode('utf-8'),
                        file_name="song.csv", mime='text/csv',
                        key='download-csv')
