=================
**multithreader**
=================

Overview
--------

Execute Python functions with multithreading.

Usage
-----

Installation:

.. code-block:: BASH

    pip3 install multithreader
    # or
    python3 -m pip install multithreader

Example:

.. code-block:: PYTHON

    def test_function(
        iterator,
        items
    ) -> int:
        """Sum two numbers."""
        print(iterator)
        sleep(1)
        return items['a'] + items['b']

    # Import multithreader.
    from multithreader import threads

    # Define arguments.
    items = {
        'a': 1,
        'b': 2
    }

    # Define iterators.
    iterators = [1, 2, 3, 4, 5]

    # Execute function with multithreading.
    results = threads(
        test_function,
        iterators,
        items,
        thread_num=int(sys.argv[1])
    )

    # Print results.
    print(results)

Full Example
------------

- `List AWS Hosted Zones in an organization <https://github.com/fer1035/pypi-multithreader/blob/main/examples/org_hosted_zones.py>`_
