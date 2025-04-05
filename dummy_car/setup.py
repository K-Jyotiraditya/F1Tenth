from setuptools import setup

package_name = 'dummy_car'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='f1tenth rrt',
    license='UPenn',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_car_node = dummy_car.dummy_car_node:main',
        ],
    },
)
