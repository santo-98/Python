import scipy.io.wavfile
import pydub
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

mp3_8 = pydub.AudioSegment.from_mp3("8.mp3")
mp3_7 = pydub.AudioSegment.from_mp3("7.mp3")

mp3_8.export("8.wav", format="wav")
mp3_7.export("7.wav", format="wav")

rate,audData = scipy.io.wavfile.read("7.wav")

fft_out = fft(audData)

print(np.abs(fft_out))
print(fft_out)
plt.plot(audData, np.abs(fft_out))
plt.show()
