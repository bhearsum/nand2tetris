from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup


setup(
    name="n2ttools",
    version="0.5",
    description="nand2tetris compiler/vm/assembler/etc toolchain",
    author="Ben Hearsum",
    author_email="ben@hearsum.ca",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    test_suite="tests",
    url="https://github.com/bhearsum/nand2tetris/tree/main/n2ttools",
    license="MPL-2.0",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "n2tasm = n2ttools.assembler:main"
        ],
    },
)
