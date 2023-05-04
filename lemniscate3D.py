#importing necessary libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt




#Parametric equations in cartesian coordinates
r   = 5 #ray
t = np.linspace(0, 2* np.pi, 100) #timeline/period

x = 2*r*np.sqrt(2)*((np.sin(t))/(1+(np.cos(t)**2)))
y = 2*r*np.sqrt(2)*((np.sin(t)*np.cos(t))/(1+(np.cos(t)**2)))
z = 2*r*np.sqrt(2)*np.cos(t)


fig = plt.figure('Parametric curve')
ax  = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, '-r', linewidth = 3)

coords = []
for i in range(len(t)):
    coords.append([x[i],y[i],z[i]])

csvFormat = ""
for point in coords:
    csvFormat = csvFormat + str(point[0])+";" + str(point[1])+";" + str(point[2])+"\n"
print(csvFormat)

f = open("test.csv", "w")
f.write(csvFormat)
f.close()

#setting the labels
ax.set_xlabel('X', fontsize = 12)
ax.set_ylabel('Y', fontsize = 12)
ax.set_zlabel('Z', fontsize = 12)

plt.title('Parametric Curve', fontsize = 14)
# plt.show()