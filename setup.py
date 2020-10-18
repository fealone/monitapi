from setuptools import find_packages
from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    entry_points="""
        [console_scripts]
        monitapi=monitapi:commands
    """
)
