import numpy as np
import sys
import os
import pickle 
import scipy.io as sio
import pandas as pd
from nscf_scraper import nscf_scraper


N = int(sys.argv[1])
name = sys.argv[2]

os.chdir('0')
frame = nscf_scraper('nscf.out')
frames = [frame]
os.chdir('..')

for k in range(1,N):
    os.chdir(str(k))
    frame = nscf_scraper('nscf.out')
    frames.append(frame)
    os.chdir('..')

result = pd.concat(frames)
matrix = result.values
sio.savemat(name+'_Ek.mat', {'matrix':matrix})


