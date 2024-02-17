from wata.pointcloud.pcd import PointCloudProcess
import os

def obtain_cur_path():
    return os.path.dirname(os.path.abspath(__file__))

def show_kitti():
    cur_path = obtain_cur_path()
    PointCloudProcess.show_pcd(os.path.join(cur_path, "resources/pcd/000000.bin"))

def print_my_name():
    print("wangtao")
