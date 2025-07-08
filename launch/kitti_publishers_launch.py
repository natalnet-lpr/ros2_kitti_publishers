#!/usr/bin/python3

from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
from ament_index_python.packages import get_package_share_directory
import os
import launch_ros.actions
import pathlib

def generate_launch_description():
    cfg = os.path.join(
        get_package_share_directory('ros2_kitti_publishers'),
        'settings.yaml'
        )
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_kitti_publishers',
            executable='kitti_publishers',
            output='screen',
            parameters=[
                cfg
            ],
         ),
    ])