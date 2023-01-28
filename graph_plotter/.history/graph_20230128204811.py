import matplotlib.pyplot as plt

x1 = [2, 4, 5]
y2 = [ 2, 3, 6]

plt.plot(x1,y2, label = 'Line 1')
plt.plot(x1, y2 , color='green', linestyle='dashed', linewidth=3, marker='o')

x2 = [1, 2, 3]
y2 = [ 4, 5, 1]

plt.plot(x2,y2, label = 'Line 2')



plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graphs!')

plt.legend()

plt.show()