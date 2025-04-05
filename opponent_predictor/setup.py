from setuptools import setup

package_name = 'opponent_predictor'

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
    description='f1tenth opponent predictor lab',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'opponent_predictor_node = opponent_predictor.opponent_predictor_node:main',
        ],
    },
)
