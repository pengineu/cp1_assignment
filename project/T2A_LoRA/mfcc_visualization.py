import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pandas as pd

# # compare same style, different transcription
# # compare same transcription, different styles
# style_1_script_1 = "./ElevenLabs_2026-01-13_Adam1_1.wav"
# style_1_script_2 = "./ElevenLabs_2026-01-13_Adam2_1.wav"
# style_2_script_1 = "./ElevenLabs_2026-01-13_Alice1_1.wav"
# '''
# script 1 : "What I mean is that mr Goodwood came out in the steamer with me."
# script 2 : "When she was old enough to ask them they were mostly about peter Pan."
# '''

style_1_script_1 = "./민정1.wav"
style_1_script_2 = "./민정2.wav"
style_2_script_1 = "./해솔1.wav"
style_2_script_2 = "./해솔2.wav"
style_3_script_1 = "./채운1.wav"
style_3_script_2 = "./채운2.wav"
style_4_script_1 = "./신재1.wav"
style_4_script_2 = "./신재2.wav"
style_5_script_1 = "./선우1.wav"
style_5_script_2 = "./선우2.wav"

def get_mfcc(file_path, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfcc[2:]

def plot_mfcc(mfcc, title='MFCC Mean and Standard'):
    mfcc_mean = np.mean(mfcc, axis=1)
    mfcc_std = np.std(mfcc, axis=1)

    plt.figure(figsize=(10, 4))
    plt.errorbar(np.arange(len(mfcc_mean)), mfcc_mean, yerr=mfcc_std, fmt='o')
    plt.title(title)
    plt.xlabel('MFCC Coefficients')
    plt.ylabel('Values')
    plt.show()
    return None


def plot_combined_mfcc(mfccs, labels):
    plt.figure(figsize=(12, 6))

    # X축 인덱스 (0~12)
    x = np.arange(mfccs[0].shape[0])
    # 시각적 구분을 위한 색상과 오프셋(옆으로 미는 정도)
    colors = ['royalblue', 'royalblue', 'darkorange', 'darkorange', 'red', 'red', 'pink', 'pink', 'olive', 'olive']
    offsets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i, mfcc in enumerate(mfccs):
        mean = np.mean(mfcc, axis=1)
        std = np.std(mfcc, axis=1)

        # fmt='o-'로 설정하면 점들을 선으로 연결해줘서 패턴이 더 잘 보입니다.
        plt.errorbar(x + offsets[i], mean, yerr=std,
                     fmt='o-', color=colors[i], label=labels[i],
                     capsize=4, elinewidth=1.5, markersize=6, alpha=0.8)

    plt.title('MFCC Comparison: Style vs Transcription', fontsize=14)
    plt.xlabel('MFCC Coefficients (Index)', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.xticks(x)
    plt.legend()
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)

    # 0번 계수가 너무 크면 그래프가 찌그러져 보일 수 있으니
    # 필요한 경우 1번 계수부터의 범위로 자동 조정되게 함
    plt.tight_layout()
    plt.show()

# 데이터 준비
m1 = get_mfcc(style_1_script_1, n_mfcc=40)
m2 = get_mfcc(style_1_script_2, n_mfcc=40)
m3 = get_mfcc(style_2_script_1, n_mfcc=40)
m4 = get_mfcc(style_2_script_2, n_mfcc=40)
m5 = get_mfcc(style_3_script_1, n_mfcc=40)
m6 = get_mfcc(style_3_script_2, n_mfcc=40)
m7 = get_mfcc(style_4_script_1, n_mfcc=40)
m8 = get_mfcc(style_4_script_2, n_mfcc=40)
m9 = get_mfcc(style_5_script_1, n_mfcc=40)
m10 = get_mfcc(style_5_script_2, n_mfcc=40)

# mfccs = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
# mfcc_means = [np.mean(m, axis=1) for m in mfccs]
# column_names = [f'MFCC_{i}' for i in range(40)]
# mfcc_df = pd.DataFrame(mfcc_means, columns=column_names)

labels = [
    'Minjung_1', 'Minjung_2',
    'Haesol_1', 'Haesol_2',
    'Chaeun_1', 'Chaeun_2',
    'Sinjae_1', 'Sinjae_2',
    'Sunwoo_1', 'Sunwoo_2'
]

# mfcc_df.insert(0, 'Label', labels)
#
# print(mfcc_df)
# mfcc_df.to_csv('mfcc_features.csv', index=False)




plot_combined_mfcc([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10],
                   ['Style1, Script1', 'Style1, Script2', 'Style2, Script1', 'Style2, Script2',
                    'Style3, Script1', 'Style3, Script2', 'Style4, Script1', 'Style4, Script2',
                    'Style5, Script1', 'Style5, Script2'])