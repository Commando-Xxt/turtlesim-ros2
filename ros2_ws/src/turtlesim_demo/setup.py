from setuptools import setup

package_name = 'turtlesim_demo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/demos.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='AI4 turtlesim manipulation demo.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'draw_square = turtlesim_demo.draw_square:main',
        ],
    },
)
