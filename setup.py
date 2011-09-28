from setuptools import setup, find_packages

readme = open('README.rst').read()
version = "0.1.0"

setup(
    name="getfeed",
    version="0.1.0",
    license="MIT License",
    author="Bernardo B. Marques",
    author_email="bernardo.fire@gmail.com",
    description="Factories for plain old Python objects.",
    url="https://github.com/rodrigomanhaes/calve_machine",
    keywords="python feed rss",
    packages=find_packages(),
    long_description=readme,
    classifiers=[
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development :: Libraries',
        ],
    install_requires=[
        "py-notify",
        "feedparser"
    ],
    entry_points="""
    [console_scripts]
    getfeed = getfeed:main
    """
    )

