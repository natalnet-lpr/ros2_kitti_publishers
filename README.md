# ROS2 Kitti Dataset Publishers

ROS2 node to publish [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php) datasets as ROS2 messages
(based on [this implementation](https://github.com/umtclskn/ros2_kitti_publishers)).

This code was tested on:

- Ubuntu 24.04 LTS
- ROS2 Jazzy

## __Install__

1. Download or clone this repo under your __<ROS2_Workspace>/src__ folder. ( i.e: `/home/user/ros2_ws/src`)
2. Source your ROS2 installation:
   
   `$ source /opt/ros/<ros2_distro>/setup.bash`

3. Build the package:
   
   `$ cd /home/user/ros2_ws`

   `$ colcon build`

## __Setup__

1. Download the KITTI datasets
2. Supposing `/home/user/kitti` is the root folder containing all KITTI datasets, change the file `config/settings.yaml` to use an specific dataset.
   For example, if you want to use `2011_09_29_drive_0071_sync`:

- `kitti_prefix: "/home/user/kitti"`
- `kitti_date: "2011_09_29"`
- `kitti_dataset: "2011_09_29_drive_0071_sync"`

## __Launching__

1. Source your ROS2 workspace:
   
   `$ source /home/user/ros2_ws/install/setup.bash`

2. Launch the node
   
   `$ ros2 launch ros2_kitti_publishers kitti_publishers_launch.py`

Use RViz2 with the config file `"default.rviz"` to visualize the data being published.