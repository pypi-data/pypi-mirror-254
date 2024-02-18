import os
import shutil

import setuptools


def setup() -> None:
    with open('requirements.txt') as text_file:
        requirements = text_file.read().splitlines()

    version = '1.0.0'

    setuptools.setup(
        packages=setuptools.find_packages(),
        install_requires=requirements,
        python_requires='>=3.8.0',
        include_package_data=True,
        author='ErnisMeshi',
        version=version,
        name='yolov7-face-landmark-detection',
    )



if __name__ == '__main__':
    setup()
