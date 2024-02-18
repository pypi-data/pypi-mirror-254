import numpy as np
import os

snspd = np.loadtxt(os.getcwd()+'/SNSPD_1PC_2MHz_signal_1.28MHz_sync.txt').astype(np.int64)
np.savetxt(os.getcwd()+'/tag_signal.txt' , snspd[snspd[:,0]==4,1],fmt="%d")
np.savetxt(os.getcwd()+'/tag_sync.txt' , snspd[snspd[:,0]==2,1],fmt="%d")