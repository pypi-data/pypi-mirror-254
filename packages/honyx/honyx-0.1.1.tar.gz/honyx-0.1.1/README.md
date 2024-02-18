# HONyx

HONyx is a Python package for generating and analyzing Higher-Order Networks models

- **Source:** https://gitlab.univ-nantes.fr/queyroi-f/honyx
- **Bug reports:** https://gitlab.univ-nantes.fr/queyroi-f/honyx/-/issues


Usage
-----
```python
>>> import honyx
>>> import networkx as nx

>>> sequences = [['a','b','r','a','c','a','d','a','b','r','a']]
>>> fon2 = honyx.generate_hon(sequences, "fix-order", max_order = 2)

>>> pos = nx.spring_layout(fon2)
>>> node_cols = ['blue' if len(v)==1 else 'green' for v in fon2.nodes()]
>>> nx.draw(fon2, pos = pos, with_labels=True, node_size=1000, node_color = node_cols, alpha=0.5)
>>> nx.draw_networkx_edge_labels(fon2, pos, edge_labels = nx.get_edge_attributes(fon2,'weight'))
```
![Order 2 Network](https://gitlab.univ-nantes.fr/queyroi-f/honyx/-/raw/main/docs/ex_fon2_readme.png "Order 2 Network")

```python
>>> honyx.pagerank_hon(fon2)
{'a': 0.40849881734049087,
 'd': 0.14318783763461537,
 'c': 0.1478373488011564,
 'r': 0.15427265837422358,
 'b': 0.14620333784951386}
```

Citing
------

To cite HONyx, please use the following publication:

    Julie Queiros, François Queyroi (2023). 
    Construction de Réseaux d'Ordre Supérieur à partir de Traces : Méthodes et Outils. 
    https://hal.science/hal-04085138 

[PDF](https://hal.science/hal-04085138/) [BibTeX](https://hal.science/hal-04085138v1/bibtex)


Install
-------
Using  Python 3.8, 3.9, or 3.10.

Install the latest version of HONyx:

    $ pip install honyx

Required dependancies include [NetworkX](https://networkx.org/), [Numpy](https://numpy.org/) and [Scipy](https://scipy.org/).

License
-------

Released under the MIT license (see `LICENSE.txt`)::

    Copyright (C) 2004-2023 HONyx Developers
    Julie Queiros <julie.queiros@univ-nantes.fr>
    François Queyroi <francois.queyroi@univ-nantes.fr>
    Simon Artus <simon.artus@etu.univ-nantes.fr>