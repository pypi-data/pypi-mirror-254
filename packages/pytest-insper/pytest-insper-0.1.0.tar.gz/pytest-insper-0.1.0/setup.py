import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytest-insper",
    version="0.1.0",
    author="Andrew Kurauchi",
    author_email="andrewTNK@insper.edu.br",
    description="Pytest plugin for courses at Insper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/insper-education/pytest-insper",
    project_urls={
        "Bug Tracker": "https://github.com/insper-education/pytest-insper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        'pytest11': [
            'insper = pytest_insper',
        ],
    },
    install_requires=[
        'pytest',
    ],
)
