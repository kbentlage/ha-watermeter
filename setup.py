from setuptools import setup

setup(
    name='watermeter',
    version='1.0.0',
    packages=['watermeter'],
    entry_points={
        'console_scripts': [
            'watermeter = watermeter.__main__:main'
        ]
    },
)