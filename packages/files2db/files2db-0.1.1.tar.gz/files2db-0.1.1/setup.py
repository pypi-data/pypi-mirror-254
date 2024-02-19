import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
DESCRIPTION = (HERE / "README.md").read_text()

setup(
    name = 'files2db',
    version = '0.1.1',
    description = 'Migration from local files to database made simple!',
    long_description = DESCRIPTION,
    long_description_content_type="text/markdown",
    url = 'https://github.com/FluffyDietEngine/files-2-db',
    author = 'Santhosh Solomon',
    author_email = 'solomon.santhosh@gmail.com',
    license = 'Apache License 2.0',
    platforms='any',
    classifiers = [
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
    ],
    packages=find_packages('src'),
    package_dir={"":"src"},
    include_package_data=True,
    entry_points={
        "console_scripts":[
            "files-2-db=files2db.main:main",
        ]
    },
    keywords='data-migration, mysql, csv, data-engineering, automation',
    install_requires=[
        "polars==0.20.6",
        "PyMySQL==1.1.0"
    ]
)
