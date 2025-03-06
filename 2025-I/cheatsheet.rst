Course cheatsheet
=================

This file contains a cheatsheet with hints, instructions and boilerplate to deal with \
the most common tasks of the course.

.. sectnum::

Installing conda and git
---------------------------

* Download Anaconda or miniconda from this `link <https://www.anaconda.com/download/success>`_
* Download Git from this `link <https://git-scm.com/downloads/win>`_

This video explains at detail:

.. image:: https://img.youtube.com/vi/C5MoZQTZ5Uc/maxresdefault.jpg
    :alt: Installation
    :target: https://www.youtube.com/watch?v=C5MoZQTZ5Uc


Cloning the course repo and installing a conda environment
-------------------------------------------------------------

#. Open the anaconda prompt.
#. Navigate to the folder where you want to clone the course repository using ``cd``.
#. Clone the repo doing: :code:`git clone https://github.com/tyrael147/MSPC14.git`.
#. Go to the freshly created course repository: :code:`cd MSPC14`.
#. Create a conda environment called `mspc14-class` using this code: :code:`conda create -n mspc14-class python=12`.
#. Activate the new environment using this code: :code:`conda activate mspc14-class`
#. Use `pip` to install the required dependencies running this code: :code:`pip install -r 2025-I/25-02-2025/requirements.txt`.
  In case of error, verify that you are located in MSPC14 and run the code again. 
#. Run jupyter lab with this code: :code:`jupyter lab`

This video explains at detail:

.. image:: https://img.youtube.com/vi/Pb9aYrESax4/maxresdefault.jpg
    :alt: Usage
    :target: https://www.youtube.com/watch?v=Pb9aYrESax4
