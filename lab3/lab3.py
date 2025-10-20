import matplotlib.pyplot as plt 
import scipy.signal # модуль обработки сигналов
#from scipy.io import wavfile 
import soundfile as sf # модуль для считывания звука

import numpy as np

zummArray, zummSecunds = sf.read('zums.ogg')

print(f'zummSecunds >>> ${zummSecunds}  zummArray >>> ${zummArray}')

if zummArray.ndim > 1:
    zummArray = zummArray[:, 0]

time = np.arange(0, len(zummArray)) / zummSecunds

# создать график с обычным звуком

plt.figure()

plt.plot(time, zummArray)
plt.title("обычный звук файл бл")
plt.xlabel("Время")
plt.ylabel("dB")

plt.show()


# доабвить шум на сигнал звуковой и создать граф

def add_noise(data, noise_level=0.05):
    if data.ndim > 1:
        noisy_data = np.zeros_like(data)
        for i in range(data.shape[1]):
            noise = noise_level * np.random.normal(0, 1, len(data))
            noisy_data[:, i] = data[:, i] + noise
    else: 
        noise = noise_level * np.random.normal(0, 1, len(data))
        noisy_data = data + noise

    noisy_data = np.clip(noisy_data, -1.0, 1.0)

    return noisy_data


timeWithNoise = add_noise(zummArray, 0.05)
# чем больше урвоень шума тем силньее исказится спектр >>> ауф

plt.plot(time, timeWithNoise)
plt.title("звук с шумом")
plt.xlabel("Время")
plt.ylabel("dB")

plt.show()
