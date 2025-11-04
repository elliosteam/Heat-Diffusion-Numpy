import numpy as np 
import matplotlib.pyplot as plt 

n = 50 

temp = np.zeros(n)
temp[n//2] = 100


for _ in range(200):
    temp[1:-1] += 0.1 * (temp[:-2] - 2*temp[1:-1] + temp[2:])

plt.style.use("ggplot")
plt.plot(temp)
plt.title("Heat shit")
plt.show()
plt.savefig("Heat_Diffusion.png")