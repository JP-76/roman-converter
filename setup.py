from setuptools import setup, find_packages

setup(
    name="roman_converter",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Uma biblioteca para converter números inteiros em algarismos romanos.",
    author="João Pedro Spinassé",
    author_email="joaopedro.spinasse@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
)
