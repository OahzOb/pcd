import open3d as o3d
import numpy as np
from decorators import time_this, deprecated


def radius_gen(num_points:int = 1000) -> np.ndarray:
    return (np.random.rand(num_points) * 2 - 1) * np.pi


@time_this
def ball_gen_random_sample(num_points:int = 10000) -> o3d.geometry.PointCloud:
    points = np.random.rand(num_points, 3) * 2 - 1
    dists = np.linalg.norm(points, axis=1)
    keys = np.where(dists <= 1.0)
    points_valid = points[keys]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points_valid)
    return pcd


@deprecated(version='0.1', reason='Non-uniform Sampling')
@time_this
def ball_gen_only_surface_radians(num_points:int = 1000) -> o3d.geometry.PointCloud:
    rzs = radius_gen(num_points)
    rxs = radius_gen(num_points)
    z = np.sin(rzs)
    res = np.cos(rzs)
    x = np.cos(rxs) * res
    y = np.sin(rxs) * res
    points = np.column_stack((x, y, z))
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd


@time_this
def ball_gen_only_surface(num_points:int = 1000) -> o3d.geometry.PointCloud:
    points = np.random.normal(size=(num_points, 3))
    dists = np.linalg.norm(points, axis=1, keepdims=True)
    points_normalized = points / dists
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points_normalized)
    return pcd


def ball_gen(type: str = 'random_sample', num_points:int = 10000) -> o3d.geometry.PointCloud:
    if type == 'random_sample':
        pcd = ball_gen_random_sample(num_points=num_points)
    elif type == 'only_surface':
        pcd = ball_gen_only_surface(num_points=num_points)
    else:
        raise TypeError(f"Unsupported generation method: {type}!")
    return pcd


def pcd_generator(type: str = None, num_points: int = 1000) -> o3d.geometry.PointCloud:
    if not type:
        points = np.random.rand(num_points, 3)
    else:
        x = np.random.rand(num_points) * 2 - 1
        res = 1 - x ** 2
        y = (np.random.rand(num_points) * 2 - 1) * res
        z = np.sqrt(1 - x ** 2 - y ** 2)
        points = np.column_stack((x, y, z))
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd


def show_pcd(pcd: o3d.geometry.PointCloud) -> None:
    o3d.visualization.draw_geometries([pcd])
    return None


def extract_pcd_boundary(pcd: o3d.geometry.PointCloud):
    pcd_t = o3d.t.geometry.PointCloud(pcd.points)


if __name__ == '__main__':
    pcd = ball_gen(type='only_surface', num_points=20000)
    show_pcd(pcd)