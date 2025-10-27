import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

def plot_mel_spectrogram(y, sr, n_mels=128, fmax=8000):
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=fmax)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', fmax=fmax)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.show()

if __name__ == "__main__":
    for audio_path in os.listdir('.'):
        if audio_path.endswith('.wav'):
            y, sr = librosa.load(audio_path, sr=None)
            plot_mel_spectrogram(y, sr)