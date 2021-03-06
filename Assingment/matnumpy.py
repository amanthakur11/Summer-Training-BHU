import numpy as np
import matplotlib.pyplot as pl

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
pl.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
pl.show()



