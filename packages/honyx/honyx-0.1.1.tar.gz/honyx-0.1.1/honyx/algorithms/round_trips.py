"""
Module to compute round trips probabilities in Higher-order Networks
"""

__all__ = ["average_round_trip"]

def average_round_trip(G):
    """
    Compute the average probability to do a round trip on the graphs in two steps

    Parameters
    ----------
    G : NetworkX DiGraph 
        A Higher-Order Network (Networkx' Digraph)

    Returns
    -------
    avg_rt: float
        Average probability to do a round trip on the graph
    """
    # TODO more than two steps
    tot_roundtrip = 0.
    nb_singletrip = 0.
    for src1, tgt1, _ in G.out_edges(data=True):
        if len(src1) == 1:
            nb_singletrip += 1.
            total_w_tgt1 = 0.
            roundtrip_w_tgt1 = 0.
            nb_roundtrip_tgt1 = 0
            for _, tgt2, data2 in G.out_edges(tgt1, data=True):
                total_w_tgt1 += data2['weight']
                if tgt2[-1] == src1[-1]:
                    roundtrip_w_tgt1 = data2['weight']
                    nb_roundtrip_tgt1 += 1
            assert nb_roundtrip_tgt1<=1, f'multiple roundtrip between {src1} and {tgt2}'
            if total_w_tgt1 > 0:
                tot_roundtrip += roundtrip_w_tgt1 / total_w_tgt1

    avg_rt = tot_roundtrip / nb_singletrip
    return avg_rt