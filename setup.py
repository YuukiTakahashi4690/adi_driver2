from setuptools import setup, find_packages
from glob import glob
import os

package_name = 'adis_driver2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('./launch/*.launch.py')),
    ],
    zip_safe=True,
    maintainer='YuukiTakahashi4690',
    maintainer_email='19c1068aq@s.chibakoudai.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'scripts_main = '+ package_name +'.scripts_main:ros_main',
            'adis16465_node = adi_driver2.adis16465_node:main'        
        ],
    }
)