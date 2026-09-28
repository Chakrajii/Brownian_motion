from functions import vacf
import matplotlib.pyplot as plt

iteration = 100

mod_vacf = []
for i in range(iteration):
    mod_vacf.append(vacf[i])

plt.plot(mod_vacf)
plt.savefig('output.png')
