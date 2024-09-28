import mne

# .vhdrファイルのパスを指定（.eegは自動的に読み込まれます）
vhdr_file = '/Users/takayukiono/Desktop/MyProject/neuro/Delayed-Auditory-Feedback-EEG/data/sub-01.vhdr'

# EEGデータを読み込む
raw = mne.io.read_raw_brainvision(vhdr_file, preload=True)

# 基本情報を表示
print(raw.info)

# データの簡単なプロット（データの一部を表示）
raw.plot(duration=5, n_channels=10)

# 最初の5秒間のデータを表示
start, stop = raw.time_as_index([0, 5])  # 0秒から5秒まで
data, times = raw[:, start:stop]
print(data)
print(times)