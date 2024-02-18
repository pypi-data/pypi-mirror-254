from glob import glob
from os.path import splitext, basename

from setuptools import setup, find_packages

with open("CHANGELOG.md", "r") as f:
    version = f.readline().split(" ")[1]

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="airflowkit",
    version=version,
    description="AirflowKit",
    url="https://github.com/m-letourneur/pyconfita.git",
    email="marc.letourneur.dev@gmail.com",
    license_file="LICENSE",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8, <3.12",
    install_requires=[
        "apache-airflow[google]>=2.5.3",
        "apache-airflow-providers-google",
    ],
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
)
