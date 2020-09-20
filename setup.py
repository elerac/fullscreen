from setuptools import setup, find_packages

setup(
    name='fullscreen',
    version='1.0.0',
    description='Display the image in full screen',
    url='https://github.com/elerac/fullscreen',
    author='Ryota Maeda',
    author_email='maeda.ryota.elerac@gmail.com',
    license='MIT',
    py_modules=['fullscreen'],
    entry_points={'console_scripts': ['fullscreen= fullscreen:main']},
    packages=find_packages()
)
