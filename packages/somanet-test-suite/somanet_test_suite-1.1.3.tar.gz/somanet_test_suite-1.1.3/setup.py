import os
import re

import setuptools
from setuptools.command.install import install

package_name = "somanet_test_suite"  # "sts"

package_to_install = [
    package_name,
    package_name + '.daq',
    package_name + '.psu',
    package_name + '.communication',
    package_name + '.communication.ethercat',
    package_name + '.communication.can',
    package_name + '.communication.uart',
    package_name + '.sanssouci',
    package_name + '.hardware_description_builder',
]

class InstallEOL(install):
    user_options = [
        ('custom-name=', None, 'Custom package name'),
    ]

    def initialize_options(self):
        self.custom_name = "somanet_test_suite"
        global package_name
        package_name = self.custom_name
    def run(self):
        install.run(self)

def get_version(path):
    with open(path, 'r') as f:
        version_file = f.read()
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M).group(1)


def get_requirements():
    requirements = []
    if os.path.isfile('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = f.read().splitlines()
    return requirements


def get_long_description():
    with open("README.rst", "r") as f:
        long_description = f.read()
    return long_description


_package_dir = {'': 'src/'}
if package_name != "somanet_test_suite":
    _package_dir = {package_name: 'src/somanet_test_suite'}

setuptools.setup(
    # cmdclass={
    #     'install': InstallEOL
    # },
    name=package_name,
    version=get_version('src/somanet_test_suite/__init__.py'),
    package_dir=_package_dir,
    packages=package_to_install,
    install_requires=get_requirements(),
    license='MIT',
    author='Synapticon GmbH',
    author_email='hstroetgen@synapticon.com',
    description="A collection of different scripts and drivers (PSU, EtherCAT, Labjack,...)",
    long_description=get_long_description(),
    python_requires=">=3.6",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Hardware :: Hardware Drivers',
    ],
    keywords=[
        'power supply unit',
        'psu',
        'daq',
        'Labjack',
        'Elektro-Automation',
        'EtherCAT',
        'IgH',
        'Synapticon',
        'CANopen',
        'CAN'
        'SOEM'
    ],
    scripts=[
        'src/somanet_test_suite/hardware_description_builder/somanet_hw_description_builder',
        'src/somanet_test_suite/psu/psu_controller',
    ]
)
