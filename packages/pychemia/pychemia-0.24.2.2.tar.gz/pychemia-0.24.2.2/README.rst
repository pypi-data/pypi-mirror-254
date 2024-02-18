PyChemia, Python Framework for Materials Discovery and Design
=============================================================

PyChemia is an open-source Python Library for materials structural
search. The purpose of the initiative is to create a method agnostic
framework for materials discovery and design using a variety of methods
from Minima Hoping to Soft-computing based methods. PyChemia is also a
library for data-mining, using several methods to discover interesting
candidates among the materials already processed.

The core of the library is the Structure python class, it is able to
describe periodic and non-periodic structures. As the focus of this
library is structural search the class defines extensive capabilities to
modify atomic structures.

The library includes capability to read and write in several ab-initio
codes. At the level of DFT, PyChemia support VASP, ABINIT and Octopus.
At Tight-binding level development is in process to support DFTB+ and
Fireball. This allows the library to compute electronic-structure
properties using state-of-the-art ab-initio software packages and
extract properties from those calculations.

Installation
============

You can install pychemia in several ways. We are showing 3 ways of
installing PyChemia inside a Virtual environment. A virtual environment
is a good way of isolating software packages from the pacakges installed
with the Operating System. The decision on which method to use
depends if you want to use the most recent code or the package uploaded
from time to time to PyPi. The last method is particularly suited for
developers who want to change the code and get those changes operative without
an explicit instalation.


Installing with pip from pypi.org on a virtual environment
----------------------------------------------------------

This method installs PyChemia from the packages uploaded
to PyPi every month. It will provides a version of
PyChemia that is stable.

First, create and activate the virtual environment.
We are using the name ``pychemia_ve``, but that is arbitrary.

::

    python3 -m venv pychemia_ve
    source pychemia_ve/bin/activate


When the virtual environment is activated, your prompt
changes to ``(pychemia_ve)...$``. Now, install pychemia
with pip

::

    python3 -m pip install pychemia


Installing with pip from a cloned repo on a virtual environment
---------------------------------------------------------------

This method installs PyChemia from the Github repo.
The method will install PyChemia from the most recent sources.

First, create and activate the virtual environment.
We are using the name ``pychemia_ve``, but that is arbitrary.

::

    python3 -m venv pychemia_ve
    cd pychemia_ve
    source bin/activate

Second, clone the repository from GitHub

::

    git clone https://github.com/MaterialsDiscovery/PyChemia.git


Finally, install from the repo folder

::

    python3 -m pip install PyChemia


Using PyChemia from repo folder on a virtual environment
--------------------------------------------------------

This method is mostly used for development.
In this way PyChemia is not actually installed and changes to the code
will take inmediate effect.

First, create and activate the virtual environment.
We are using the name ``pychemia_ve``, but that is arbitrary.

::

    python3 -m venv pychemia_ve
    cd pychemia_ve
    source bin/activate


Clone the repository

::

    git clone https://github.com/MaterialsDiscovery/PyChemia.git


Go to repo folder, install Cython with pip and
execute ``setup.py`` to build the Cython modules.

::

    cd PyChemia
    python3 -m pip install Cython
    python3 setup.py build_ext --inplace
    python3 setup.py build


Finally, install the packages required for PyChemia to work

::

    python3 -m pip install -r requirements.txt


Set the variable ``$PYTHONPATH`` to point to PyChemia folder, in the case of bash it will be:

::

    export PYTHONPATH=`path`


On C shell (csh or tcsh)

::
    
    setenv PYTHONPATH `path`


To run the internal testsuite install ``pytest``

::

    python3 -m pip install pytest


Execute the testsuite:

::

    pytest


The output of the testsuite looks like this:

::

    =================== test session starts ===========================
    platform linux -- Python 3.11.3, pytest-7.3.0, pluggy-1.0.0
    rootdir: /gpfs20/scratch/gufranco/PyChemia
    plugins: hypothesis-6.71.0, anyio-3.6.2
    collecting 2 items                                            
    collecting 29 items                                           
    collected 67 items                                                 

    tests/test_0.py .                                            [  1%]
    tests/test_1_doctest_core.py ...                             [  5%]
    tests/test_1_doctest_crystal.py ..                           [  8%]
    tests/test_1_doctest_utils.py ....                           [ 14%]
    tests/test_3_scripts.py ....                                 [ 20%]
    tests/test_analysis.py ...                                   [ 25%]
    tests/test_code_abinit.py .....                              [ 32%]
    tests/test_code_fireball.py .                                [ 34%]
    tests/test_code_vasp.py ......                               [ 43%]
    tests/test_core.py ......                                    [ 52%]
    tests/test_crystal_kpoints.py .                              [ 53%]
    tests/test_crystal_symmetry.py .                             [ 55%]
    tests/test_db_queue.py .                                     [ 56%]
    tests/test_io.py ..                                          [ 59%]
    tests/test_population.py .....                               [ 67%]
    tests/test_population_orbitals.py .                          [ 68%]
    tests/test_searcher_clusters.py ....                         [ 74%]
    tests/test_searcher_functions.py ....                        [ 80%]
    tests/test_searcher_noncollinear.py ...                      [ 85%]
    tests/test_utils_metaheuristics.py .                         [ 86%]
    tests/test_utils_periodic.py ......                          [ 95%]
    tests/test_utils_serializer.py .                             [ 97%]
    tests/test_zexample1.py .                                    [ 98%]
    tests/test_zexample2.py .                                    [100%]

    =================== 67 passed in 54.60s ===========================


PyChemia requirements
=====================

PyChemia relies on a number of other python packages to
operate. Some of them are mandatory and they must be installed.
Other packages are optional and their absence will only constrain
certain capabilities.

Mandatory
---------

1.  Python >= 3.6
    The library is tested on Travis for Python 3.6 up to 3.9
    Support for Python 2.7 has been removed

    https://travis-ci.org/MaterialsDiscovery/PyChemia

2.  `Numpy <http://www.numpy.org/>`_  >= 1.19
    Fundamental library for numerical intensive computation in Python.
    Numpy arrays are essential for efficient array manipulation.

3.  `SciPy <http://scipy.org/>`_ >= 1.5
    Used mostly for Linear Algebra, FFT and spatial routines.

4.  `Spglib <http://spglib.sourceforge.net/>`_ >= 1.9
    Used to determine symmetry groups for periodic structures

5.  `Matplotlib <http://matplotlib.org/>`_  >= 3.3
    Used to plot band structures, densities of states and other 2D plots

6.  `PyMongo <http://api.mongodb.org/python/current/>`_ >= 3.11
    Used for structural search PyChemia relies strongly in MongoDB and its python driver.
    For the MongoDB server, any version beyond 3.11 should be fine.
    We have tested pychemia on MongoDB 4.0

7.  `psutil <https://github.com/giampaolo/psutil/>`_ >= 5.8
    Cross-platform lib for process and system monitoring in Python

8.  `netCDF4 <https://github.com/Unidata/netcdf4-python>`_ > 1.5
    Python/numpy interface to the netCDF C library


Optional
--------

1.  `nose <https://nose.readthedocs.io/en/latest/>`_ >= 1.3.7 A python
    library for testing, simply go to the source directory and execute

    nosetests -v

2.  `pytest <https://docs.pytest.org/en/latest/>`_
    Another utility for testing.

3.  `Pandas <http://pandas.pydata.org/>`_
    Library for Data Analysis used by the datamining modules

4.  `PyMC <http://pymc-devs.github.io/pymc/index.html>`_
    PyMC is a python module that implements Bayesian statistical models
    and fitting algorithms
    Important for the datamining capabilities of PyChemia

5.  `Mayavi <http://docs.enthought.com/mayavi/mayavi/>`_  >= 4.1
    Some basic visualization tools are incorporated using this library

6.  `ScientificPython <http://dirac.cnrs-orleans.fr/plone/software/scientificpython/overview/>`_  >2.6
    This library is used for reading and writing NetCDF files

7.  `pymatgen <http://www.pymatgen.org>`_ >= 2.9
    pymatgen is an excellent library for materials analysis

8.  `ASE <https://wiki.fysik.dtu.dk/ase/>`_ 
    Atomic Simulation Environment is another good library for ab-initio calculations.
    Quite impressive for the number of ab-initio packages supported

9.  `qmpy <http://oqmd.org/static/docs/index.html>`_
    The Python library behind the [Open Quantum Materials Database](http://oqmd.org).
    The OQMD is a database of DFT calculated structures.
    For the time being the database contains more than 300000 structures, with more than
    90% of them with the electronic ground-state computed.

10. `coverage <https://bitbucket.org/ned/coveragepy>`_ >= 4.0.1
    Provides code coverage analysis

11. `python-coveralls <https://github.com/z4r/python-coveralls>`_
    To submit coverage information to coveralls.io

    https://coveralls.io/github/MaterialsDiscovery/PyChemia

Documentation
=============

Instructions for installation, using and programming scripts with PyChemia
can be found on two repositories for documentation:

* Read The Docs:

   http://pychemia.readthedocs.io/en/latest

* Python Hosted:

   http://pythonhosted.org/pychemia

Documentation is hosted on `Read the Docs <https://readthedocs.org/projects/pychemia/>`_ also available with Short URLs `readthedocs <http://pychemia.readthedocs.io>`_ and `rtfd <http://pychemia.rtfd.io>`_

Documentation is also hosted on `Python Hosted <http://pythonhosted.org/pychemia/index.html>`_

Sources
=======

The main repository is on `GitHub <https://github.com/MaterialsDiscovery/PyChemia>`_

Sources and wheel binaries are also distrubuted on `PyPI Python.org <https://pypi.python.org/pypi/pychemia>`_ or `PyPI pypi.org <https://pypi.org/project/pychemia/>`_

Contributors
============

1.  Prof. Aldo H. Romero [West Virginia University] (Project Director)

2.  Guillermo Avendaño-Franco [West Virginia University]
    (Basic Infrastructure)

3.  Adam Payne [West Virginia University] (Bug fixes (Populations, Relaxators, and KPoints) )

4.  Irais Valencia Jaime [West Virginia University] (Simulation and testing)

5.  Sobhit Singh [West Virginia University] (Data-mining)

6.  Francisco Muñoz [Universidad de Chile] (PyPROCAR)

7.  Wilfredo Ibarra Hernandez [West Virginia University] (Interface with MAISE)

