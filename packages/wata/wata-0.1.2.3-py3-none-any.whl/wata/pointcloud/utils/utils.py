import numpy as np
from pathlib import Path
try:
    from load_pcd import get_points_from_pcd_file
except:
    from .load_pcd import get_points_from_pcd_file
def cut_pcd(points, pcd_range):
    x_range = [pcd_range[0], pcd_range[3]]
    y_range = [pcd_range[1], pcd_range[4]]
    z_range = [pcd_range[2], pcd_range[5]]
    mask = (x_range[0] <= points[:, 0]) & (points[:, 0] <= x_range[1]) & (y_range[0] < points[:, 1]) & (
            points[:, 1] <= y_range[1]) & (z_range[0] < points[:, 2]) & (points[:, 2] <= z_range[1])
    points = points[mask]
    return points

def get_points(path, num_features=3):
    pcd_ext = Path(path).suffix
    if pcd_ext == '.bin':
        points = np.fromfile(path, dtype=np.float32).reshape(-1, 4)
    elif pcd_ext == ".npy":
        points = np.load(path)
    elif pcd_ext == ".pcd":
        points = get_points_from_pcd_file(path, num_features=num_features)
    else:
        raise NameError("Unable to handle {} formatted files".format(pcd_ext))
    return points[:, 0:num_features]