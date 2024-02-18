from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Package to get data from cloud director'

# Setting up
setup(
    name="clouddirector",
    version=VERSION,
    author="Shubham Rawat",
    author_email="<shivamrawat829@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'lxml'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)