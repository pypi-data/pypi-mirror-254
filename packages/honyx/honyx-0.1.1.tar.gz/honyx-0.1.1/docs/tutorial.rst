Tutorial
========

..
    .. currentmodule:: honyx

This guide can help individuals commence their work with HONyx 
by providing an overview of the terminology used within the package. 

Small Example
-------------

Let's create a small dataset of sequences

.. code-block:: python

    >>> import honyx
    >>> sequences = [['a','d','e'],
    ...              ['a','d','e'],
    ...              ['d','e'],
    ...              ['b','d','e'],
    ...              ['b','d','e'],
    ...              ['b','d','e'],
    ...              ['d','f'],
    ...              ['d','f'],
    ...              ['b','d','f'],
    ...              ['b','d','f'],
    ...              ['b','d','f'],
    ...              ['b','d','f'],
    ...              ['b','d','c'],
    ...              ['b','d','c'],
    ...              ['b','d','c'],
    ...              ['c','d','c'],
    ...              ['c','d','c'],
    ...              ['c','d','c']]

A classic network of order can be used to encode the direct transitions between the items 
``[a, b, c, d, e, f]`` as follows:

.. code-block:: python

    >>> fon1 = honyx.generate_hon(sequences, "fix-order", max_order = 1)
    >>> fon1
    <networkx.classes.digraph.DiGraph object at 0x7f77e1e37d60>

It is a NetworkX DiGraph with the following attributes

.. code-block:: python

    >>> for n, d in fon1.nodes(data=True):
    ...     print(f'{n} : {d}')
    ...     for e in fon1.out_edges(n, data=True):
    ...         print(f'    {e[1]} : {e[2]}')
    ... 
    ('a',) : {'item': 'a', 'order': 1, 'count': 2}
        ('d',) : {'count': 2, 'weight': 1.0}
    ('d',) : {'item': 'd', 'order': 1, 'count': 18}
        ('e',) : {'count': 6, 'weight': 0.3333333333333333}
        ('f',) : {'count': 6, 'weight': 0.3333333333333333}
        ('c',) : {'count': 6, 'weight': 0.3333333333333333}
    ('b',) : {'item': 'b', 'order': 1, 'count': 10}
        ('d',) : {'count': 10, 'weight': 1.0}
    ('c',) : {'item': 'c', 'order': 1, 'count': 3}
        ('d',) : {'count': 3, 'weight': 1.0}
    ('e',) : {'item': 'e', 'order': 1, 'count': 0}
    ('f',) : {'item': 'f', 'order': 1, 'count': 0}

Note that ``count`` stores the number of times that a given subsequences 
occurs **followed by another item**.
(i.e. the order-1 subsequence *e* is always placed at the end of a sequence.)

Let's increase the maximum order to 2:

.. code-block:: python

    >>> fon2 = honyx.generate_hon(sequences, "fix-order", max_order = 2)
    >>> for n, d in fon2.nodes(data=True):
    ...     print(f'{n} : {d}')
    ...     for e in fon2.out_edges(n, data=True):
    ...         print(f'    {e[1]} : {e[2]}')
    ... 
    ('a',) : {'item': 'a', 'order': 1, 'count': 2}
        ('a', 'd') : {'count': 2, 'weight': 1.0}
    ('d',) : {'item': 'd', 'order': 1, 'count': 18}
        ('e',) : {'count': 6, 'weight': 0.3333333333333333}
        ('f',) : {'count': 6, 'weight': 0.3333333333333333}
        ('c',) : {'count': 6, 'weight': 0.3333333333333333}
    ('c',) : {'item': 'c', 'order': 1, 'count': 3}
        ('c', 'd') : {'count': 3, 'weight': 1.0}
    ('c', 'd') : {'item': 'd', 'order': 2, 'count': 3}
        ('c',) : {'count': 3, 'weight': 1.0}
    ('b',) : {'item': 'b', 'order': 1, 'count': 10}
        ('b', 'd') : {'count': 10, 'weight': 1.0}
    ('b', 'd') : {'item': 'd', 'order': 2, 'count': 10}
        ('f',) : {'count': 4, 'weight': 0.4}
        ('c',) : {'count': 3, 'weight': 0.3}
        ('e',) : {'count': 3, 'weight': 0.3}
    ('a', 'd') : {'item': 'd', 'order': 2, 'count': 2}
        ('e',) : {'count': 2, 'weight': 1.0}
    ('e',) : {'item': 'e', 'order': 1, 'count': 0}
    ('f',) : {'item': 'f', 'order': 1, 'count': 0}

We now have order-2 memory nodes! For example, *('c', 'd')* encodes the event
"being in *d* coming from *c*". 
*('b', 'd')*, *('c', 'd')* or *('d',)* are different representations of item *d*.
The only possibility in this case is to go back to *c* with probability (i.e. `weight`) 1.
Note that memory-nodes are still regular nodes. 
Nodes of order 1 or higher are encoded with `tuple(str)`.


.. note::
    Fiedx-order networks of `max_order` 2 or higher still contain memory-nodes of lower order.
    In the literature, these models are sometimes called "multi-order networks" [1]_. 
    Since the maximum order is a priori *fixed* and to avoid confusion with *variable-order networks* [2]_ 
    (see next example), we decided to call these networks *fixed-order networks*.  

Now we can compare order-1 and order-2 networks. 
For example, order-2 better captures the round trips found in the dataset.

The `average_round_trip` function can be used to compute the average roundtrip probability *i.e.* 
if I start at any order-1 node *(x, )* and I follow any outgoing edge, what is the probability of visiting a representation of *x*?

.. code-block:: python

    >>> honyx.average_round_trip(fon1)
    0.2222222222222222
    >>> honyx.average_round_trip(fon2)
    0.3333333333333333


Wikispeedia Example
-------------------

This example uses trajectories extract from the Wikispeedia game [3]_, 
where a player tries to get from one page to another with as few hyperlink clicks as possible.
The dataset can be found in ``examples/wikispeedia_top100.ngram``. 
We restrict  ourselves to the top 100 most visited articles (as done in [1]_)

.. code-block:: python

    >>> import honyx
    >>> sequences = honyx.read_sequences('./examples/wikispeedia_top100.ngram')
    >>> sequences[4]
    ['Europe', 'North_America', 'United_States', 'President_of_the_United_States']

Here the items are not just letters, but the titles of Wikipedia articles.
Let's try to find the optimal order for a fixed-order network using Shotles method [1]_

.. code-block:: python

    >>> opt_fon = honyx.generate_hon(sequences, "optimal-order", max_order = 5, ct=0.001)
    >>> opt_fon.graph['max_order']
    1

We will not try orders beyond 5 and we will use a confidence threshold of 1/1000. 
According to this model, there are now indirect dependencies in this dataset 
(the graph attribute `max_order` stores the actual maximum order among the memory nodes)

We can also try to construct a variable-order network [2]_

.. code-block:: python

    >>> von = honyx.generate_hon(sequences, "variable-order", max_order = 6)
    >>> von.graph['max_order']
    4
    >>> von.number_of_nodes()
    2301

Here, we find sequential dependencies of order 4. 
Note that the total number of memory nodes is less than 
for because a 4 order network  not all possible memory-node are included
in the variable-order network.

We can wonder about the impact of these indirect dependencies on graph mining algorithms. 
For example, using the PageRank centrality measure, the top 10 most important pages in the order 1 network are

.. code-block:: python

    >>> pr_fon1 = honyx.pagerank_hon(opt_fon)
    >>> sorted_pr_fon1= {k: v for k, v in sorted(pr_fon1.items(), key=lambda item: item[1], reverse=True)[:10]}
    >>> for item, val in sorted_pr_fon1.items():
    ...     print(f'{item} : {round(val, 3)}')
    ... 
    United_States : 0.066
    Europe : 0.035
    United_Kingdom : 0.029
    Africa : 0.028
    Earth : 0.023
    Computer : 0.021
    Microsoft : 0.02
    World_War_II : 0.019
    England : 0.018
    North_America : 0.018
    
and in the variable-order network:

.. code-block:: python

    >>> pr_von = honyx.pagerank_hon(von)
    >>> sorted_pr_von = {k: v for k, v in sorted(pr_von.items(), key=lambda item: item[1], reverse=True)[:10]}
    >>> for item, val in sorted_pr_von.items():
    ...     print(f'{item} : {round(val, 3)}')
    ... 
    United_States : 0.058
    Europe : 0.03
    Microsoft : 0.026
    Africa : 0.023
    World_War_II : 0.023
    United_Kingdom : 0.022
    Computer : 0.021
    Agriculture : 0.02
    Earth : 0.019
    Internet : 0.019

.. note::
    `pagerank_hon` give the PageRank per items. The PageRank of an item is the sum of the pagerank
    of the memory-nodes representating the same item. 
    Moreover, we used an unbiaised method for higher-order network [4]_.

Bibliography
------------
    .. [1] Scholtes, Ingo.
      "When is a network a network?
      Multi-order graphical model selection in pathways and temporal networks."
      In Proceedings of the 23rd ACM SIGKDD international conference
      on knowledge discovery and data mining,
      pp. 1037-1046. 2017.

    .. [2] Saebi, Mandana, Jian Xu, Lance M. Kaplan, Bruno Ribeiro, and Nitesh V. Chawla.
      "Efficient modeling of higher-order dependencies in networks:
      from algorithm to application for anomaly detection."
      EPJ Data Science 9, no. 1 (2020): 15.


    .. [3] Robert West, Joelle Pineau, and Doina Precup: 
       Wikispeedia: An Online Game for Inferring Semantic Distances between Concepts. 
       21st International Joint Conference on Artificial Intelligence (IJCAI), 2009. 

    .. [4] Coquidé, Célestin, Julie Queiros, and François Queyroi. 
      "PageRank computation for Higher-Order networks." 
      Complex Networks & Their Applications X: Volume 1, 
      Proceedings of the Tenth International Conference on Complex Networks 
      and Their Applications COMPLEX NETWORKS 2021 10. 
      Springer International Publishing, 2022.
      https://arxiv.org/pdf/2109.03065