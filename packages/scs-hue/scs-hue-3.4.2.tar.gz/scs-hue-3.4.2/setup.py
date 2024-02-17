"""
Created on 9 Nov 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://packaging.python.org/tutorials/packaging-projects/
https://packaging.python.org/guides/single-sourcing-package-version/

https://stackoverflow.com/questions/65841378/include-json-file-in-python-package-pypi
https://stackoverflow.com/questions/45147837/including-data-files-with-setup-py
"""

import codecs
import os
import setuptools


# --------------------------------------------------------------------------------------------------------------------

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            return line.split("'")[1]
    else:
        raise RuntimeError("Unable to find version string.")


# --------------------------------------------------------------------------------------------------------------------

with open('README.md') as fh:
    long_description = fh.read()

with open('requirements.txt') as req_txt:
    required = [line for line in req_txt.read().splitlines() if line]

# packages = setuptools.find_packages('src'), scs_philips_hue.config.paths

setuptools.setup(
    name="scs-hue",
    version=get_version("src/scs_philips_hue/__init__.py"),
    author="South Coast Science",
    author_email="contact@southcoastscience.com",
    description="Connecting Philips Hue light bulbs to South Coast Science environmental data sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/south-coast-science/scs_philips_hue",
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    package_data={'scs_philips_hue': ['**/*.csv', '**/*.json', '**/*.me']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX",
    ],
    scripts=[
        'src/scs_philips_hue/aws_client_auth.py',
        'src/scs_philips_hue/aws_mqtt_subscriber.py',
        'src/scs_philips_hue/bridge.py',
        'src/scs_philips_hue/bridge_address.py',
        'src/scs_philips_hue/chroma.py',
        'src/scs_philips_hue/chroma_conf.py',
        'src/scs_philips_hue/desk.py',
        'src/scs_philips_hue/desk_conf.py',
        'src/scs_philips_hue/domain_conf.py',
        'src/scs_philips_hue/join.py',
        'src/scs_philips_hue/light.py',
        'src/scs_philips_hue/node.py',
        'src/scs_philips_hue/run_chroma.sh',
        'src/scs_philips_hue/uds_receiver.py',
        'src/scs_philips_hue/upnp_conf.py',
        'src/scs_philips_hue/user.py'
    ],
    install_requires=required,
    platforms=['any'],
    python_requires='>3.6',
    extras_require={
        'dev': [
            'pypandoc'
        ]
    }
)
