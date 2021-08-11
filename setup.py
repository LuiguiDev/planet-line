from setuptools import setup

setup (
    name='crud_blue',
    version='0.1',
    blue_modules=['crud_blue'],
    intall_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        crud_blue=crud_blue:enter
    ''',
)
