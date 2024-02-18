import os
import re
import sys

from setuptools import find_packages, setup

org = 'PEtab-dev'
repo = 'petab_select'


def read(fname):
    """Read a file."""
    return open(fname).read()


def absolute_links(txt):
    """Replace relative petab github links by absolute links."""

    raw_base = f"(https://raw.githubusercontent.com/{org}/{repo}/main/"
    embedded_base = f"(https://github.com/{org}/{repo}/tree/main/"
    # iterate over links
    for var in re.findall(r'\[.*?\]\((?!http).*?\)', txt):
        if re.match(r'.*?.(png|svg)\)', var):
            # link to raw file
            rep = var.replace("(", raw_base)
        else:
            # link to github embedded file
            rep = var.replace("(", embedded_base)
        txt = txt.replace(var, rep)
    return txt


# 3.7.1 for NumPy, 3.8 for `typing.get_args`
minimum_python_version = '3.8'
if sys.version_info < tuple(map(int, minimum_python_version.split('.'))):
    sys.exit(f'PEtab Select requires Python >= {minimum_python_version}')

# read version from file
__version__ = ''
version_file = os.path.join('petab_select', 'version.py')
# sets __version__
exec(read(version_file))  # pylint: disable=W0122 # nosec

ENTRY_POINTS = {
    'console_scripts': [
        'petab_select = petab_select.cli:cli',
    ]
}

# project metadata
# noinspection PyUnresolvedReferences
setup(
    name='petab_select',
    version=__version__,
    description='PEtab Select: an extension to PEtab for model selection.',
    long_description=absolute_links(read('README.md')),
    long_description_content_type="text/markdown",
    # author='The PEtab Select developers',
    # author_email='dilan.pathirana@uni-bonn.de',
    url=f'https://github.com/{org}/{repo}',
    packages=find_packages(exclude=['doc*', 'test*']),
    install_requires=[
        # TODO minimum versions
        'more-itertools',
        'numpy',
        'pandas',
        'petab',
        'pyyaml',
        #'python-libsbml>=5.17.0',
        #'sympy',
        # required for CLI
        'click',
        'dill',
        # plotting
        #'matplotlib>=2.2.3',
        #'seaborn',
    ],
    include_package_data=True,
    python_requires=f'>={minimum_python_version}',
    entry_points=ENTRY_POINTS,
    extras_require={
        'test': [
            'pytest >= 5.4.3',
            'pytest-cov >= 2.10.0',
            'amici >= 0.11.25',
            'fides >= 0.7.5',
            # FIXME
            'pypesto > 0.2.13',
            # 'pypesto @ git+https://github.com/ICB-DCM/pyPESTO.git@develop#egg=pypesto',
        ],
        'doc': [
            'sphinx>=3.5.3,<7',
            'sphinxcontrib-napoleon>=0.7',
            'sphinx-markdown-tables>=0.0.15',
            'sphinx-rtd-theme>=0.5.1',
            'recommonmark>=0.7.1',
            # pin until ubuntu comes with newer pandoc:
            # /home/docs/checkouts/readthedocs.org/user_builds/petab-select/envs/63/lib/python3.11/site-packages/nbsphinx/__init__.py:1058: RuntimeWarning: You are using an unsupported version of pandoc (2.9.2.1).
            # Your version must be at least (2.14.2) but less than (4.0.0).
            'nbsphinx==0.9.1',
            'nbconvert<7.5.0',
            'ipython>=7.21.0',
            'readthedocs-sphinx-ext>=2.2.5',
            'sphinx-autodoc-typehints',
        ],
    },
)
