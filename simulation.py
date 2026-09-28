# This will mainly consist of Making of the Gaussian Noise. And the Eulerian - Maruyan scheme

import numpy as np 
from numpy import random 
import pandas as pd 

noise = random.normal(loc = 0 , scale = 1 , size = 10000)

Velocity = []
Velocity.append(0)

gamma = 1 
dt = 0.1
v = 0 

time = []
time.append(0)
t= 0


for i in noise:
    v = v - gamma*v+dt + np.sqrt(dt)*i
    t = t+dt
    Velocity.append(v)
    time.append(t)

data = {
    'Velocity' : Velocity,
    'Time' : time
}

df = pd.DataFrame(data)
df.to_csv("Motion.csv" , index = False)