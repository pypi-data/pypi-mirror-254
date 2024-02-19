import numpy as np
import matplotlib.pyplot as plt

def draw_3d_sphere(radius):
    # 创建一个3D图形对象
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 生成球体坐标
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    # 计算球体顶点的x、y、z坐标
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)

    # 绘制3D球体
    ax.plot_surface(x, y, z, color='blue', alpha=0.6)

    # 设置坐标轴标签
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # 显示图形
    plt.show()


def plot_3d_cylinder(radius, height):
    # 创建一个3D图形对象
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
 
    # 生成底面的坐标
    theta = np.linspace(0, 2 * np.pi, 100)  # 圆周角度
    theta, z = np.meshgrid(theta, np.linspace(0, height, 100))  # z坐标从0到高度
 
    # 计算底面的x、y坐标
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
 
    # 绘制底面
    ax.plot_surface(x, y, z, color='blue', alpha=0.6)
 
    # 绘制侧面
    # 从底面到底点
    x_lines = np.concatenate((x[0, :], [0]))
    y_lines = np.concatenate((y[0, :], [0]))
    z_lines = np.concatenate((z[0, :], [0]))
    ax.plot(x_lines, y_lines, z_lines, color='green')
 
    # 设置坐标轴标签
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
 
    # 设置坐标轴比例相同
    ax.set_aspect('auto')
 
    # 显示图形
    plt.show()


def plot_3d_cone(radius, height):
    # 创建一个3D图形对象
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
 
    # 生成底面的坐标
    theta = np.linspace(0, 2 * np.pi, 100)  # 圆周角度
    z = np.zeros_like(theta)  # 底面z坐标为0
 
    # 计算底面的x、y坐标
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
 
    # 绘制底面
    ax.plot(x, y, z, color='blue', alpha=0.6)
 
    # 生成侧面的坐标
    # 注意：侧面是由底面的一系列点与顶点连接形成的
    theta = np.linspace(0, 2 * np.pi, 100)
    theta, h = np.meshgrid(theta, np.linspace(0, height, 100))
    x = radius * np.cos(theta) * (h / height)
    y = radius * np.sin(theta) * (h / height)
    z = h
 
    # 绘制侧面
    ax.plot_surface(x, y, z, color='green', alpha=0.6)
 
    # 绘制底面边缘
    # 不需要单独绘制底面边缘，因为已经通过plot_surface绘制了底面
 
    # 绘制顶点
    ax.scatter([0], [0], [height], color='red')
 
    # 设置坐标轴标签
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
 
    # 设置坐标轴比例相同
    ax.set_aspect('auto')
 
    # 显示图形
    plt.show()

 