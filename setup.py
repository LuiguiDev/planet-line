from setuptools import setup

setup (
    name='crud',
    version='0.1',
    blue_modules=['crud'],
    intall_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        crud=crud:cli
    ''',
)
