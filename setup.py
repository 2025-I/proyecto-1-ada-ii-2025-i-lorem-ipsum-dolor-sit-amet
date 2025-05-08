from setuptools import find_packages, setup

setup(
    name="proyecto-ada",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=8.3.5",
        "setuptools>=80.3.1",
        "wheel>=0.46.1",
    ],
    python_requires=">=3.9",
)