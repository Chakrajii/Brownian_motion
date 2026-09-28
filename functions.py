# This will include the functions like like Velocity autocorrelation fucntion , and other things

import pandas as pd 
import numpy as np

df = pd.read_csv('Motion.csv')
arr = df['Velocity']

vacf = []
N = len(arr)
for i in range(N):
    vacf.append(np.mean(arr[i:] * arr[:N-i]))

vacf = np.array(vacf)
vacf = vacf/vacf[0]

