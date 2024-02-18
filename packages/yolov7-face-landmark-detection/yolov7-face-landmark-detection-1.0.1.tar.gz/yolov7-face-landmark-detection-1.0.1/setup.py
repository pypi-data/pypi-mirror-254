import os
import shutil

import setuptools


def setup() -> None:
    requirements = ['matplotlib >= 3.2',
                    'numpy >= 1.18',
                    'opencv-python >= 4.1',
                    'PyYAML >= 5.3',
                    'scipy >= 1.4',
                    'Pillow',
                    'torch >= 1.7',
                    'torchvision >= 0.8',
                    'tqdm >= 4.41',
                    'tensorboard >= 2.4',
                    'seaborn >= 0.11',
                    'pandas',
                    'onnxruntime == 1.10',
                    'pycocotools >= 2.0']
    version = '1.0.1'

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
