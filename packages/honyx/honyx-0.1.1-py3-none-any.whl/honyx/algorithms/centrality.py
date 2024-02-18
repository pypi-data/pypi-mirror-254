from networkx import pagerank


__all__ = ["pagerank_hon"]


def pagerank_hon(
        G, 
        alpha=0.85, 
        max_iter=100,
        tol=1.0e-6,
        weight='weight'
        ):
    """Returns the PageRank of the items in the Higher-Order Network.

    References
    ----------
    .. [1] Coquidé, Célestin, Julie Queiros, and François Queyroi. 
      "PageRank computation for Higher-Order networks." 
      Complex Networks & Their Applications X: Volume 1, 
      Proceedings of the Tenth International Conference on Complex Networks 
      and Their Applications COMPLEX NETWORKS 2021 10. 
      Springer International Publishing, 2022.
      https://arxiv.org/pdf/2109.03065
    
    Parameters
    ----------
    G : graph
      A NetworkX digraph encoding the Higher-order Network

    alpha : float, optional
      Damping parameter for PageRank, default=0.85.

    max_iter : integer, optional
      Maximum number of iterations in power method eigenvalue solver.

    tol : float, optional
      Error tolerance used to check convergence in power method solver.
      The iteration will stop after a tolerance of ``len(G) * tol`` is reached.

    weight : key, optional
      Edge data key to use as weight.  If None weights are set to 1.

    Returns
    -------
    item_pr : dictionary
       Dictionary of items with PageRank as value
    """

    ## get order-1 memory-nodes
    o1_nodes = [n for n,d in G.nodes(data=True) if d['order']==1]
    ## create personalisation vector s.t. random teleportation occurs 
    ## uniformaly at random on order-1 memory nodes
    o1_vector = {n:1./len(o1_nodes) for n in o1_nodes}

    pr = pagerank(G, alpha, o1_vector, max_iter, tol, None, weight)
    ## the PageRank value of an item is the sum of the PageRank of 
    ## memory-nodes representing this item.
    item_pr = {}
    for n, val in pr.items():
        if n[-1] not in item_pr:
            item_pr[n[-1]] = 0.
        item_pr[n[-1]] += val
    return item_pr