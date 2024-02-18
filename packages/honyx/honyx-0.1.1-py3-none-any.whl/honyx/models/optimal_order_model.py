"""
Module to create an Optimal-order network.
"""

from math import log
from collections import defaultdict
#import time

#from networkx import all_simple_paths, has_path
from scipy.stats import chi2

from networkx import DiGraph

from honyx.models.fix_order_model import FixOrderModel

######################################################################################
def _number_of_paths(graph, node, k=1):
    """Return the number of paths of length k in the given graph starting from node.
    Used to compute the Degrees Of Freedom in the Optimal Order model.
    
    Parameters
    ----------
    graph: DiGraph
        A NetworkX digraph (Fon_1 representation of input sequence)
    
    """

    if k==1:
        return graph.out_degree(node)
    if f'npath{k}' in graph.nodes[node].keys():
        return graph.nodes[node][f'npath{k}']
    res = 0
    for edge in graph.out_edges(node):
        res += _number_of_paths(graph, edge[1], k-1)
    graph.nodes[node][f'npath{k}'] = res
    return res

######################################################################################

class OptimalOrderModel(FixOrderModel):
    '''
    After building a Fixed-Order model, find the order <= max_order that best fits
    the observed sequences using a likelihood-ratio test.

    Attributes
    ----------
    ct: float
        confidence threshold for the likelihood-ratio test 
    fon1 : networkx.DiGraph
        The networkX directional graph representing the FON_1 calculated at the beginning.
    d_o_f : dict[int, int]
        The degrees of freedom (value) for each order (key).
    logl : dict[int, float]
        The log likelihood (value) for each order (key).
    best_order : int
        The found best order.

    References
    ----------
    .. [1] Scholtes, Ingo.
      "When is a network a network?
      Multi-order graphical model selection in pathways and temporal networks."
      In Proceedings of the 23rd ACM SIGKDD international conference
      on knowledge discovery and data mining,
      pp. 1037-1046. 2017.
    '''

    def __init__(self, max_order, min_support = 1, ct = 0.001):
        """Initialises the OptimalOrderModel."""
        FixOrderModel.__init__(self, max_order, min_support)
        self.ct = ct

        self.fon1 = DiGraph()
        self.d_o_f = {}
        self.logl = {}
        self.best_order = 1

    ######################################################################################
    def fit(self, sequences):
        """Extends the FixOrderModel to try to find the best order

        Parameters
        ----------
        sequences : list[list[str]]
            The sequences to fit the model from.

        Returns
        -------
        contexts : defaultdict[tuple[str, ...], defaultdict[str, int]]
            The valid context found for the optimal order.

        """
        FixOrderModel.fit(self, sequences)
        order1contexts = {}
        for context, adj_r in self.valid_contexts.items():
            if len(context)==1:
                order1contexts[context[0]] = adj_r
        self.fon1 = DiGraph(order1contexts)

        # start_time = time.time()
        ## compute d_o_f for order 1 to self.MaxOrder
        self.compute_degrees_of_freedom()

        ## compute and save log-likelihood for order 1
        self.logl[1] = self.log_likelihood(1)
        ## look for best order
        for curr_ord in range(2,self.max_order+1):
            logl_o = self.log_likelihood(curr_ord)
            self.logl[curr_ord] = logl_o
            ratio_l_o = 2.*(logl_o - self.logl[curr_ord-1])
            diff_dof = self.d_o_f[curr_ord] - self.d_o_f[curr_ord-1]
            chi2_p = 1.-chi2.cdf(ratio_l_o, df=diff_dof)
            if chi2_p < self.ct:
                self.best_order = curr_ord

        to_remove = [r for r, adj_r in self.valid_contexts.items() if len(r) > self.best_order]
        for context in to_remove:
            del self.valid_contexts[context]
        return self.valid_contexts

    #################################################################
    def log_likelihood(self, order=1):
        """Returns the log likelihood for the given order.

        Parameters
        ----------
        order : int
            The order to get the log likelihood from.

        Returns
        -------
        prob : float
            The log likelihood.
        """

        prob = 0.
        for seq in self.sequences:
            ## Eq 4
            prob_t = 0.
            # print(f'{seq}')
            for i in range(len(seq)-1):
                id_s_context: int = max(0,i-order+1)
                context = tuple(seq[id_s_context:(i+1)])
                r_context = self.valid_contexts[context]
                p_context = r_context[seq[i+1]] / sum(r_context.values())
                prob_t += log(p_context)
            prob += prob_t
        return prob

    #################################################################
    def compute_degrees_of_freedom(self):
        """Set the degrees of freedom regarding the number of nodes."""
        nb_item = self.fon1.number_of_nodes()

        self.d_o_f[0] = nb_item - 1
        for k in range(self.max_order):
            np_k = 0
            non_zero_p = 0
            for node in self.fon1.nodes:
                np_n = _number_of_paths(self.fon1, node, k+1)
                np_k += np_n
                if np_n > 0:
                    non_zero_p += 1
            self.d_o_f[k+1] = self.d_o_f[k] + (np_k - non_zero_p)

    #################################################################
    def get_name(self):
        """
        Overrides to return the name of the model.

        Returns
        -------
        name : str
            The name of the model.
        """
        return 'optimal_fon'

    ######################################################################################
    def get_params_str(self, short=False):
        """
        Overrides to return the parameters of the model.

        Parameters
        ----------
        short : bool
            If the parameters should not display the max_order and the min_support.

        Returns
        -------
        params : str
        """
        base_params = super().get_params_str(short)
        if short:
            return f"ct:{self.ct}"
        return (
            base_params
            + f";ct:{self.ct}"
        )
