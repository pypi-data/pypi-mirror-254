import os
from setuptools import setup, find_packages
from Cython.Build import cythonize

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
with open('syinfo/_version.py') as f:
    exec(f.read())

# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    # "tabulate",
    # "getmac",
    # "GPUtil",
    # "PyYAML",
    # "psutil",  # causing error
    # "scapy"
    "tabulate==0.9.0",
    "getmac==0.9.4",
    "GPUtil==1.4.0",
    "PyYAML==6.0.1",
    "psutil==5.9.5",
    "scapy==2.5.0",
]

setup(
    name='syinfo',
    version=__version__,

    description="A Python package to get device and network information.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Mohit Rajput",
    author_email="mohitrajput901@gmail.com",
    maintainer="Mohit Rajput",
    maintainer_email="mohitrajput901@gmail.com",

    url='https://github.com/MR901/sys_info',
    keywords=[],

    # license="Apache 2.0",

    zip_safe=False,
    install_requires=install_requires,

    packages=find_packages(),
    # ext_modules=cythonize("sys_info/*.pyx"),  #include_path=[...]), # ValueError: 'sys_info/*.pyx' doesn't match any files
    # Check
    # - https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html
    # - https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#multiple-cython-files-in-a-package

    include_package_data=False,

    classifiers=[
        # "Development Status :: 1 - Alpha",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        # 'License :: OSI Approved :: Apache Software License',
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
    platforms=['any'],  #'any'
    python_requires='>=3.6',

    # scripts=[
    #     "sys_info/constants.py",
    #     "sys_info/device_info.py",
    #     "sys_info/__init__.py",
    #     "sys_info/__main__.py",
    #     "sys_info/network_info.py",
    #     "sys_info/search_network.py",
    #     "sys_info/sys_info.py",
    #     "sys_info/utils.py",
    #     "sys_info/_version.py",
    # ],
    py_modules=["syinfo"],
    # package_dir={"": "sys_info"},

    entry_points={
        'console_scripts': [
            'syinfo=syinfo.__main__:main',
            # 'wiom=who_is_on_my_wifi:main',
            # 'who-is-on-my-wifi=who_is_on_my_wifi:main',
        ],
    },

)
