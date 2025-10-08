from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mnet_client', 'mnet_client.base', 'mnet_client.client'],
    package_dir={'': 'src'},
)

setup(**d)