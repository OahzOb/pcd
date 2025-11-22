import open3d as o3d
import numpy as np
import time

mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
mesh_sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.2)
mesh_sphere.paint_uniform_color([0.1, 0.1, 0.7])

initial_transform = np.eye(4)
initial_transform[0, 3] = 0.02

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh_sphere)
vis.add_geometry(mesh_frame)
frame = 0
while True:
    print(frame)
    if frame > 1000:
        initial_transform[0, 3] *= -1
        print(initial_tranform[0, 3])
        frame = 0
    if frame % 100 == 0:
        mesh_sphere.transform(initial_transform)
        vis.update_geometry(mesh_sphere)
        vis.poll_events()
        vis.update_renderer()
    else:
        frame += 1

vis.destroy_window()
