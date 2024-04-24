'''import matplotlib

matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()
#подготовительный процесс
ax = plt.axes(projection="3d")  # создание осей
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')  # подписать оси

print('1 - Построить пирамиду \n2 - Построить куб \n3 - Построить шар')
c = int(input('Введите число '))

if c == 1:
    a = int(input('Длина основания - '))
    h = int(input('Высота - '))
    ax.set_xlim(1, a + 25) #пределы осей
    ax.set_ylim(1, a + 25)
    ax.set_zlim(1, h + 25)
    v = np.array(
        [[0, 0, 0],
         [0, a, 0],
         [a, a, 0],
         [a, 0, 0],
         [a / 2, a / 2, h]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
    verts = [
        [v[0], v[1], v[4]],
        [v[0], v[3], v[4]],
        [v[2], v[1], v[4]],
        [v[2], v[3], v[4]],
        [v[0], v[1], v[2], v[3]]]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='g', alpha=.25))

    plt.show()'''


from ipywidgets import interact, IntSlider
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm

@interact(a=IntSlider(min=1, max=100, step=1, value=50),
          b=IntSlider(min=1, max=100, step=1, value=50),
          h=IntSlider(min=1, max=100, step=1, value=50))
def p(a, b, h):
    fig = plt.figure()
    ax = plt.axes(projection="3d")  # создание осей
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')  # подписать оси

    ax.set_xlim(1, a + 25)
    ax.set_ylim(1, b + 25)
    ax.set_zlim(1, h + 25)
    v = np.array(
        [[0, 0, 0],
         [0, b, 0],
         [a, b, 0],
         [a, 0, 0],
         [a / 2, b / 2, h]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
    verts = [
        [v[0], v[1], v[4]],
        [v[0], v[3], v[4]],
        [v[2], v[1], v[4]],
        [v[2], v[3], v[4]],
        [v[0], v[1], v[2], v[3]]]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='g', alpha=.25))
    plt.show()


@interact(a=IntSlider(min=1, max=100, step=1, value=50),
          b=IntSlider(min=1, max=100, step=1, value=50),
          h=IntSlider(min=1, max=100, step=1, value=50))
def k(a, b, h):
    v = np.array(
        [[0, 0, 0],
         [0, b, 0],
         [a, b, 0],
         [a, 0, 0],
         [0, 0, h],
         [0, b, h],
         [a, b, h],
         [a, 0, h]])
    fig = plt.figure()
    ax = plt.axes(projection="3d")  # создание осей
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')  # подписать оси

    ax.set_xlim(1, a + 25)
    ax.set_ylim(1, b + 25)
    ax.set_zlim(1, h + 25)
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
    verts = [
        [v[0], v[1], v[5], v[4]],
        [v[0], v[4], v[7], v[3]],
        [v[7], v[3], v[2], v[6]],
        [v[2], v[6], v[5], v[1]],
        [v[0], v[1], v[2], v[3]],
        [v[4], v[5], v[6], v[7]]
    ]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='g', alpha=.25))
    plt.show()



@interact(r=IntSlider(min=1, max=50, step=1, value=25))
def b(r):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')  # подписать оси

    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_zlim(-50, 50)

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    ax.plot_surface(x, y, z, color='cyan', alpha=0.7)
    plt.show()


