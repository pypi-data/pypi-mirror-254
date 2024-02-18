 
******************************
Generate Higher-Order Networks
******************************

.. automodule:: utils
    :noindex: 

Available models
----------------

In the sidebar

Example
-------

.. code-block:: python

    >>> import honyx
    >>> sequences = [['a','b','r','a','c','a','d','a','b','r','a']]
    >>> honyx.generate_hon(sequences, "fix-order", max_order = 1)
    DiGraph with 5 nodes and 7 edges
    >>> honyx.generate_hon(sequences, "fix-order", max_order = 2)
    DiGraph with 12 nodes and 14 edges
    >>> honyx.generate_hon(sequences, "variable-order", max_order = 3)
    DiGraph with 5 nodes and 7 edges


See Also
--------

.. autosummary::
    :toctree: generated/

    generate_hon
