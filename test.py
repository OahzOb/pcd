import open3d as o3d
import numpy as np
import time
import logging
import os

log_file = 'test.log'
if os.path.exists(log_file):
    os.unlink(log_file)
logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_file, level=logging.DEBUG)

logger.info("Here goes the creation of meshes.")
mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
mesh_sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.2)
mesh_sphere.paint_uniform_color([0.1, 0.1, 0.7])

logger.info("Defining a transfer matrix.")
initial_transform = np.eye(4)
initial_transform[0, 3] = 0.002
logger.debug(f"This is the matrix:\n{initial_transform}")

logger.info("Starting renderer...")
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh_sphere)
vis.add_geometry(mesh_frame)
frame = 1
logger.debug("Into the loop")
while True:
    time.sleep(0.01)
    if frame > 1000:
        logger.info("Reversing the ball.")
        initial_transform[0, 3] *= -1
        frame = 0
    mesh_sphere.transform(initial_transform)
    vis.update_geometry(mesh_sphere)
    vis.poll_events()
    vis.update_renderer()
    frame += 1

vis.destroy_window()
