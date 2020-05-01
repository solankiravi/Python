from matplotlib import pyplot as plt
from matplotlib import style

from numpy import genfromtxt

url = 'E:\\FL_insurance_sample.csv'
data = genfromtxt(url,delimiter=' ')

plt.plot(data)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()