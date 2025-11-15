import matplotlib.pyplot as plt
plt.subplot(1,2,1) # the figure has 1 row, 2 columns, and this is the first plot
plt.plot([1,2,3,4,5],[1,2,5,10,7], "r--", marker='|')
plt.grid(linestyle='--')
plt.subplot(1,2,2) # the figure has 1 row, 2 columns, and this is the second plot
plt.plot([1,2,3,4,5],[7,2,5,10,3], "g--", marker='X')
plt.grid()
plt.suptitle("Anchan")
plt.savefig('1.png')