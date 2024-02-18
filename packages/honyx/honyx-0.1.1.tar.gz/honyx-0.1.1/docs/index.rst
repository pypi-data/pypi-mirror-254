HONyx's documentation
=====================

HONyx is a Python package for creating and studying higher-order networks. It provides:

-  the generation of HONs as `NetworkX <https://networkx.org/>` graphs according to 
   various models found in the literature.
-  data mining algorithms customized for Higher-order networks.
   However, the current selection is limited!

Citing
------

To cite HONyx, please use the following publication:

Julie Queiros, François Queyroi. 
Construction de Réseaux d'Ordre Supérieur à partir de Traces : Méthodes et Outils. 
https://hal.science/hal-04085138/, 2023. 

.. only:: html

   `PDF <https://hal.science/hal-04085138/>`_
   `BibTeX <https://hal.science/hal-04085138v1/bibtex>`_

Audience
--------

The audience for HONyx includes mathematicians, physicists, biologists,
computer scientists, and social scientists. The package is introduced in [Queiros2023]_ (in French). 
Higher-Order networks models are discussed various studies, including [Saebi20]_, [Scholtes17]_, [Xu16]_.
The mining algorithms for these networks are investigated in [Coquide2021]_ and [Queiros2022]_ as well as the aforementioned articles..

License
-------

.. include:: ../LICENSE

Bibliography
------------

.. [Queiros2023]  Julie Queiros, François Queyroi. 
   Construction de Réseaux d'Ordre Supérieur à partir de Traces : Méthodes et Outils. 
   https://hal.science/hal-04085138/, 2023. 

.. [Coquide2021] Coquidé, Célestin, Julie Queiros, and François Queyroi. 
   "PageRank computation for Higher-Order networks." 
   Complex Networks & Their Applications X: Volume 1, Proceedings of the Tenth International 
   Conference on Complex Networks and Their Applications COMPLEX NETWORKS 2021 10. 
   Springer International Publishing, 2022.

.. [Queiros2022] Queiros, Julie, Célestin Coquidé, and François Queyroi. 
   "Toward random walk-based clustering of variable-order networks." 
   Network Science 10.4 (2022): 381-399.

.. [Saebi20] Saebi Mandana, Jian Xu, Lance M. Kaplan, Bruno Ribeiro, and Nitesh V. Chawla.
   "Efficient modeling of higher-order dependencies in networks:
   from algorithm to application for anomaly detection."
   EPJ Data Science 9, no. 1 (2020): 15.

.. [Scholtes17] Scholtes, Ingo. 
   "When is a network a network? Multi-order graphical model selection in pathways 
   and temporal networks." 
   Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery 
   and data mining. 2017.

.. [Xu16] Jian Xu, Thanuka L. Wickramarathne, and Nitesh V. Chawla.
   "Representing higher-order dependencies in networks."
   Science Advances 2, no. 5 (2016): e1600028.


.. toctree::
   :maxdepth: 1
   :hidden:

   tutorial
   references/index
