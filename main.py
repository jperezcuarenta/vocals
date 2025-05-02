from basic_pitch.inference import Model
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH
import os


def main():
    params = {
        'audio_path_list': [os.path.join('inputs', 'hqmo.mp3')],
        'output_directory': os.getcwd(),
        'save_midi': True,
        'sonify_midi': True,
        'save_model_outputs': False,
        'save_notes': True,
        'model_or_model_path': Model(ICASSP_2022_MODEL_PATH),
        'onset_threshold': 0.5,
        'frame_threshold': 0.3,
        'minimum_note_length': 127.70,
        'minimum_frequency': 250,
        'maximum_frequency': 1200}
    predict_and_save(**params)

if __name__ == "__main__":
    main()