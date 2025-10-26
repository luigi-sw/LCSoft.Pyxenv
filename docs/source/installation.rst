Installation
============

Requirements
------------
* Python ≥ 3.8
* Windows, Linux or macOS

From PyPI (stable)
------------------
.. code-block:: console

   $ pip install pyxenv

From source (development)
-------------------------
.. code-block:: console

   $ git clone https://github.com/seu-usuario/pyxenv.git
   $ cd pyxenv
   $ python -m venv venv
   $ source venv/bin/activate      # Windows: venv\Scripts\activate
   $ pip install -e .[dev]

Verify
------
.. code-block:: console

   $ pyxenv --help