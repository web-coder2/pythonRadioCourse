import numpy as np
import matplotlib.pyplot as plt

a = 5 # 5 амплитуда 
omega = ( 2 * np.pi ) * 2 # 2 герца
phi = 2
t_0 = 0
t_n = 10

t_step = 0.1

t_array = np.arange(t_0, t_n, t_step)

y_array = []

for i in t_array:
    y = a * np.sin((omega * i) + phi)
    y_array.append(y)

plt.plot(t_array, y_array)
plt.show()
