import numpy as np
import matplotlib.pyplot as plt

gain = 1.5


usilitel = 0.6

# чем больше usilitel тем больше на спектре он увидится

t = np.linspace(0, 10, 1000)

input_signal = np.sin(2 * np.pi * 1 * t)
output_signal = np.zeros_like(input_signal)


for i in range(1, len(t)):
    usilitelSignal = usilitel * output_signal[i-1]
    output_signal[i] = gain * (input_signal[i] + usilitelSignal)


plt.figure(figsize=(10, 4))
plt.plot(t, input_signal, label='перывй сигнал')
plt.plot(t, output_signal, label='Выходжной сигнал')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.title('Модель системы с обратной связью')
plt.show()
