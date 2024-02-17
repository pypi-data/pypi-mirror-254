import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='qlogs',  
    version='0.0.7',
    author="Chris Dunne",
    author_email="contact@chrisdunne.net",
    description="A package for querying log files for evidence of compromise.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisdunne/qlogs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['qlogs=src.qlogs:main'],
    },
    install_requires  = [],
    include_package_data=True,
 )