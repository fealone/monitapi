from importlib.machinery import SourceFileLoader

from setuptools import find_packages
from setuptools import setup


version = SourceFileLoader('version', 'src/monitapi/version.py').load_module()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    version=version.version,
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    entry_points={
        "console_scripts": ["monitapi=monitapi:commands"]
    }
)
