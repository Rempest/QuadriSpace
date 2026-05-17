from setuptools import setup
 
package_name = 'geometry_dimension'
 
setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raempest',
    maintainer_email='thehuman130410@gmail.com',
    description='ROS2 node publishing Vector3 and Quaternion messages',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'geometry_dimension = geometry_dimension.geometry:main',
        ],
    },
)
 
