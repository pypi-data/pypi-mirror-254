from setuptools import setup, find_packages

with open("pyproject.toml", 'r') as infile:
    for i in range(3):
        line = infile.readline()
    VERSION = line[11:-2]

DESCRIPTION = 'Yasik language compiler'

# Setting up
setup(
    name="yasik",
    version=VERSION,
    author="Ruslan Shaiakhmetov",
    author_email="ruslan.shaiakhmetov@unibo.it",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'language', 'DSL'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
