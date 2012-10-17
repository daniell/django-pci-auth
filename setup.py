from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    include_package_data=True,
    install_requires=[
#        'django-newauth',
        'django-axes',
    ],
    name='django-pci-auth',
    version=VERSION,
)