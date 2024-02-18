from setuptools import setup
import pathlib

from infralib import __version__ as version

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='infralib',
    version=version,
    description='Simulation Environments for Large-Scale Infrastructure Management',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords='simulation-environment, reinforcement-learning, optimization, resource-allocation, infrastructure-management, large-scale-systems',
    url='https://github.com/pthangeda/Infralib',
    author="Pranay Thangeda",
    author_email="contact@prny.me",
    license="MIT",
    python_requires=">=3.10.0",
    packages=['infralib']
)
