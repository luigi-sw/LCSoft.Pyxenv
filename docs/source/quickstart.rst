Quick-start
===========

1. List installed Python versions
---------------------------------
.. code-block:: console

   $ pypx list

2. Install a new CPython interpreter
------------------------------------
.. code-block:: console

   $ pypx install 3.12

3. Create a virtual environment
-------------------------------
.. code-block:: console

   $ pypx venv create myproj 3.12

4. Activate the environment
---------------------------
.. code-block:: console

   # Linux/macOS
   $ source myproj/bin/activate

   # Windows
   > myproj\Scripts\activate

5. Remove an interpreter (optional)
-----------------------------------
.. code-block:: console

   $ pypx uninstall 3.12

That’s it! Run ``pypx --help`` to see all commands.