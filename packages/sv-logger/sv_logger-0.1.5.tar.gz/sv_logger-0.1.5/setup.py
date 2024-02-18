from setuptools import setup, find_packages

setup(
    name="sv_logger",
    version="0.1.5",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT",
    description="A simple logging library for Python",
    long_description=open("README.md").read(),
    author="pternali",
    author_email="patrizio.ternali15@gmail.com",
    url="",
    requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
