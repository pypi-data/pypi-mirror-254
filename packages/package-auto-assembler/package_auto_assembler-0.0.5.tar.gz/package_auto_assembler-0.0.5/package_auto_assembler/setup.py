from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
path_to_readme = os.path.join(here, "README.md")

if os.path.exists(path_to_readme):
  with codecs.open(path_to_readme, encoding="utf-8") as fh:
      long_description = fh.read()
else:
  long_description = ''

setup(
    name="package_auto_assembler",
    packages=["package_auto_assembler"],
    install_requires=['### package_auto_assembler.py', 'nbformat', 'pyyaml', 'nbconvert', 'stdlib-list', 'pandas', 'attrs>=22.2.0'],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: Science/Research', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10', 'Programming Language :: Python :: 3.11', 'License :: OSI Approved :: MIT License', 'Topic :: Scientific/Engineering'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Kyrylo Mordan", author_email="parachute.repo@gmail.com", description="A tool to automate package creation within ci based on just .py and optionally .ipynb file.", keywords="['python', 'packaging']", version="0.0.5"
)
        