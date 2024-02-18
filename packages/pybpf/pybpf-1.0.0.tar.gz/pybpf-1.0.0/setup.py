from setuptools import setup, find_packages

setup(
    name="pybpf",
    version="1.0.0",
    packages=find_packages(),
    author="El Mehdi SLAOUI",
    package_dir={"": "./"},
    extras_require={"test": "pytest"},
    license="MIT",
)
