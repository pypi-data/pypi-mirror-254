from wata.pointcloud.pcd import PointCloudProcess
from wata.lxq.fireworks_explosion import open_app as open_fireworks
import os

def explain():
    print("--------------------------------------")
    print('wata.show_kitti : 展示kitti数据集第一帧')
    print('wata.print_name : 打印我的名字')
    print("--------------------------------------")

def obtain_cur_path():
    return os.path.dirname(os.path.abspath(__file__))

def show_kitti():
    cur_path = obtain_cur_path()
    PointCloudProcess.show_pcd(os.path.join(cur_path, "resources/pcd/000000.bin"))

def print_my_name():
    print("wangtao")

def fireworks():
    cur_path = obtain_cur_path()
    open_fireworks(ui=os.path.join(cur_path, "resources/fireworks/main.ui"),
                icon=os.path.join(cur_path, "resources/fireworks/icon.png"),
                snow=os.path.join(cur_path, "resources/fireworks/snow.gif"),
                emoji=os.path.join(cur_path, "resources/fireworks/paitou.gif"),
                fireworks=os.path.join(cur_path, "resources/fireworks/fireworks"))