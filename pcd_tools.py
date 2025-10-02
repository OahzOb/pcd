from operator import length_hint

import open3d as o3d
import numpy as np
from decorators import time_this, deprecated
import functools
from typing import List, Tuple


@time_this
def ball_gen(num_points: int = 10000, radius: float = 1.0) -> o3d.geometry.PointCloud:
    points = np.random.normal(size=(num_points, 3))
    dists = np.linalg.norm(points, axis=1, keepdims=True)
    points_normalized = points / dists * radius
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points_normalized)
    return pcd


@time_this
def cubic_gen(num_points: int = 10000, lwh: Tuple[float, ] = (1.0, 1.0, 1.0)): -> o3d.geometry.PointCloud:
    l, w, h = lwh



def show_pcd(pcd: o3d.geometry.PointCloud) -> None:
    o3d.visualization.draw_geometries([pcd])
    return None


if __name__ == '__main__':
    pcd = ball_gen(type='only_surface', num_points=20000)
    show_pcd(pcd)