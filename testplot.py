import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('testplot.csv', delimiter=',')
plt.figure()
yarr = [0]
xlinsp = np.linspace(0,469,469)
for i in range(468):
    temp = data[i][1]
    yarr.append(temp)
print(yarr)
plt.plot(xlinsp,yarr)
plt.show()