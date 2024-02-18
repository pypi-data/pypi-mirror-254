from setuptools import find_packages, setup

package_name = "lapa_commons"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "configparser>=6.0.0"
    ],
    extras_require={},
    author="Lav Sharma",
    author_email="lavsharma2016@gmail.com",
    description="Lapa commons used for reading the configuration file.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/lavvsharma/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
