import matplotlib.pyplot as plt  
import numpy as np 

x = np.linspace(-5, 5, 100)
y = 2*x + np.sin(x)**2 + 3

plt.plot(x, y)
plt.grid(True)
plt.title("Hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("po.pdf")
plt.show()

