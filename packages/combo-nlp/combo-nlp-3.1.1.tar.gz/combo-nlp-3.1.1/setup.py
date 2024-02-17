import subprocess
from setuptools import find_packages, setup

subprocess.call(['pip', 'install', '--no-deps', '--ignore-requires-python', 'git+https://gitlab.clarin-pl.eu/syntactic-tools/lambo.git#egg=lambo'])

REQUIREMENTS = [
    "absl-py~=1.4.0",
    "base58~=2.1.1",
    "cached-path~=1.3.3",
    "conllu~=4.4.1",
    "conllutils~=1.1.4",
    "dill~=0.3.6",
    "importlib-resources~=5.12.0",
    "h5py~=3.9.0",
    "overrides~=7.3.1",
    "torch~=2.0.0",
    "torchtext~=0.15.1",
    "numpy~=1.24.1",
    "pytorch-lightning~=2.0.01",
    "requests~=2.28.2",
    "tqdm~=4.64.1",
    "filelock~=3.9.0",
    "pandas~=2.1.3",
    "pytest~=7.2.2",
    "transformers~=4.27.3",
    "sacremoses~=0.0.53",
    "spacy~=3.3.1",
    "urllib3==1.26.6"
]

setup(
    name="combo-nlp",
    version="3.1.1",
    author="Maja Jablonska",
    author_email="maja.jablonska@ipipan.waw.pl",
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=['tests']),
    license="GPL-3.0",
    url='https://gitlab.clarin-pl.eu/syntactic-tools/combo',
    keywords="nlp natural-language-processing dependency-parsing",
    tests_require=['pytest', 'pylint'],
    python_requires='>=3.6',
    package_data={'combo': ['config.template.json']},
    entry_points={'console_scripts': ['combo=combo.main:main']},
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ]
)
