from setuptools import setup, find_packages

setup(
    name='iTermocil',
    version='1.0.0',
    url='https://github.com/godbout/itermocil',
    license='MIT',
    description='iTermocil for Python3',
    author='Guillaume Leclerc',
    author_email='',
    packages=find_packages(),
    py_modules=['itermocil'],
    package_data={},
    classifiers=[],
    entry_points={
        'console_scripts': [
            'itermocil = itermocil:main',
        ]
    },
    install_requires=[
        'PyYAML',
    ]
)
