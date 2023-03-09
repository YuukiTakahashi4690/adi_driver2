import os
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetLaunchConfiguration, IncludeLaunchDescription, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ld = LaunchDescription()
    
    dir = '/home/y-takahashi/ros2_ws/src/adi_driver2'
    namespace = LaunchConfiguration('namespace')
    with_filter = LaunchConfiguration('with_filter')
    with_rviz = LaunchConfiguration('with_rviz')
    with_plot = LaunchConfiguration('with_plot')
    device = LaunchConfiguration('device')
    flame_id = LaunchConfiguration('flame_id')
    burst_mode = LaunchConfiguration('burst_mode')
    publish_temperature = LaunchConfiguration('publish_temperature')
    rate = LaunchConfiguration('rate')
    publish_tf = LaunchConfiguration('publish_tf')
    publish_debug_topics = LaunchConfiguration('publish_debug_topics')

    urdf = os.path.join(
        get_package_share_directory('adi_driver2'),
        'urdf',
        'adis16465_breakout.urdf')

    # xacro_file_name = 'orne_gamma.urdf.xacro'
    # xacro_file_path = os.path.join(urdf, 'gamma', xacro_file_name)
    
    rviz_config_dir = os.path.join(get_package_share_directory('adi_driver2'), 'rviz', 'imu.rviz')

    declare_nameapace_cmd = DeclareLaunchArgument(
        'namespace', 
        default_value = '', 
        description = 'namespace'
    )

    declare_with_filter_cmd = DeclareLaunchArgument(
        'with_filter', 
        default_value = 'true', 
        description = 'use with_filter: true or false'
    )

    declare_with_rviz_cmd = DeclareLaunchArgument(
        'with_rviz', 
        default_value = 'false', 
        description = 'use with_rviz: true or false'
    )

    declare_with_plot_cmd = DeclareLaunchArgument(
        'with_plot', 
        default_value = 'false', 
        description = 'use with_plot: true or false'
    )

    declare_device_cmd = DeclareLaunchArgument(
        'device', 
        # default_value = '/dev/sensors/imu16465', 
        default_value = '/dev/ttyACM0',
        description = 'device: input full path'
    )

    declare_flame_id_cmd = DeclareLaunchArgument(
        'flame_id', 
        default_value = 'imu_link',
        # default_value = 'imu', 
        description = 'flame_id: input anything flame_id'
    )

    declare_burst_mode_cmd = DeclareLaunchArgument(
        'burst_mode', 
        default_value = 'false', 
        description = 'use burst_mode: true or false'
    )

    declare_publish_temperature_cmd = DeclareLaunchArgument(
        'publish_temperature', 
        default_value = 'false', 
        description = 'use temperature: true or false'
    )

    declare_rate_cmd = DeclareLaunchArgument(
        'rate', 
        default_value = '100', 
        description = 'rate: anything value rate'
    )

    declare_publish_tf_cmd = DeclareLaunchArgument(
        'publish_tf', 
        default_value = 'false', 
        description = 'use publish_tf: true or false'
    )

    declare_publish_debug_topics_cmd = DeclareLaunchArgument(
        'publish_debug_topics', 
        default_value = 'false', 
        description = 'use publish_debug_topics: true or false'
    )

    adis16465_node = Node(
        package='adi_driver2',
        executable='adis16465',
        # name='adis16465',
        output = 'screen', 
        # remappings=[('imu', 'imu/data_raw')]
    )

    # robot_state_publisher = Node(
    #       package='robot_state_publisher',
    #       executable='robot_state_publisher',
    #       name='robot_state_publisher',
    #       output='screen',
    #       parameters=[{'use_sim_time': False}],
    #       arguments=[urdf]
    # )

    rviz2 = Node(
          package='rviz2',
          executable='rviz2',
        #   name='rviz2',
          arguments=['-d', rviz_config_dir],
          parameters=[{'use_sim_time': False}],
          output='log',
        #   condition=IfCondition(with_rviz)
    )

    ld.add_action(adis16465_node)
    # ld.add_action(robot_state_publisher)
    ld.add_action(rviz2)

    ld.add_action(declare_nameapace_cmd)
    ld.add_action(declare_with_filter_cmd)
    ld.add_action(declare_with_rviz_cmd)
    ld.add_action(declare_with_plot_cmd)
    ld.add_action(declare_device_cmd)
    ld.add_action(declare_flame_id_cmd)
    ld.add_action(declare_burst_mode_cmd)
    ld.add_action(declare_publish_temperature_cmd)
    ld.add_action(declare_rate_cmd)
    ld.add_action(declare_publish_tf_cmd)
    ld.add_action(declare_publish_debug_topics_cmd)

    return ld

#     configured_params = LaunchConfiguration(
#         device_source_file = device, 
#         flame_id_source_file = flame_id, 
#         burst_mode_source_file = burst_mode, 
#         publish_temperature_source_file = publish_temperature, 
#         rate_source_file = rate
#     )

#     IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(xacro_file_path, 'orne_gamma.urdf.xacro')),
#             conditions = IfCondition(with_rviz), 
#             launch_arguments = {
#                 'namespace': namespace}.items() 
#     ), 
