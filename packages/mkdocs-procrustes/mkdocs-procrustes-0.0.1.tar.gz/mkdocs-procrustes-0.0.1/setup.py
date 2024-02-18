from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="mkdocs-procrustes",
    version=VERSION,
    url='https://github.com/evilnick/procrustes',
    license='',
    description='A Vanilla-framework based theme',
    author='Nick Veitch',
    author_email='nick.veitch@canonical.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'themename = procrustes',
        ]
    },
    zip_safe=False
)