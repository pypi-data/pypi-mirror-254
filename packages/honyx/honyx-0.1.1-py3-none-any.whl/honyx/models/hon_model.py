"""
Module to define a general model for Higher-order networks

Notes
-----
Code adapted from Jian Xu's code [1]_

References
----------
.. [1] Jian Xu, "HON", https://github.com/xyjprc/hon, Apr 2017

"""

from collections import defaultdict

from networkx import DiGraph

###########################################
def _longest_suffix(seqs, contexts_keys):
    """
    Returns the longest suffix of tuple seqs that exist in contexts_keys.
    
    Notes
    -----
    seqs is a suffix of itself.

    Parameters
    ----------
    seqs : tuple[str]
        A sequence of symbols to extract the longest suffix from.

    contexts_keys : KeysView[tuple[str, ...]]
        `KeysView <https://docs.python.org/3/glossary.html#term-dictionary-view>`_ 
        referencing existing sequences to compare with.
    """
    while len(seqs)>1:
        if seqs in contexts_keys:
            return seqs
        seqs = seqs[1:]
    return seqs

###########################################

class HONModel():
    """
    Abstract class for Higher-order model training based on the code of
    Xu et al. [1]_

    Notes
    -----
    Rules are tested for validity (i.e. should they be added to the
    Higher-order model?) recursively.
    The actual test of validity (is_context_valid) and the related stopping condition
    for the recursion (is_ever_valid) should be defined in the inheriting classes.

    At least :func:`is_context_valid`, :func:`is_ever_valid` and :func:`get_name` should be defined
    in any implementing class.

    Fitting the data (with ``.fit()``) is mandatory if one wants to use certain functions 
    available in the model.

    Validity can be defined in very different manners and its goal is to limit the number 
    of context we store. In a fixed-order network (FON) it is the length of a sequence for example.

    :func:`is_context_valid` will tell if a specific sequence is valid or not.

    Attributes
    ----------
    count : Optional[defaultdict[tuple[str, ...], defaultdict[str, int]]]
        Used to store store every context seen, valid or not, as key and count the number of 
        occurrences of each symbol in the key context as value.
    valid_contexts : Optional[defaultdict[tuple[str, ...], defaultdict[str, int]]]
        Used to store every valid context as key, and count the
        number of occurrences of each symbol in the key context as value.
    src_to_ext_src : Optional[defaultdict[tuple[str, ...], set[tuple[str, ...]]]]
        Used for optimisation purposes, links a context to its extended versions
    starting_points : Optional[defaultdict[tuple[str, ...], set[tuple[int, int]]]]
        Used for optimisation purposes, links to where a context has already been observed.
    sequences : list[list[str]]
        The sequences of symbols to fit the higher-order network from.
    max_order : int
        The maximum order our model can reach (might be ignored by some models).
    min_support : int
        The minimum support for a sequence to be context valid.

    References
    ----------
    .. [1] Jian Xu, "HON", https://github.com/xyjprc/hon, Apr 2017
    """

    ###########################################
    def __init__(self, max_order, min_support):
        """Builds the HONModel with no values."""

        self.count = None
        self.valid_contexts = None
        self.src_to_ext_src = None
        self.starting_points = None
        self.sequences = None
        self.max_order = max_order
        self.min_support = min_support

    def build_network(self, p_weight = False):
        """Builds a network from the contexts we have.

        Parameters
        ----------
        p_weight : bool
            Used to normalise the weight between nodes of the graph if true.

        Returns
        -------
        graph : defaultdict[tuple[str, ...], dict[tuple[str, ...], float]]
            A dictionary that can be transformed into a directional graph.

            Each context links to a dictionary of next contexts with their probabilities to hop to.
        """
        # Not sure about the float in the def
        graph = defaultdict(dict)
        for seq, count_seq in self.valid_contexts.items():
            supp_s = sum(count_seq.values())
            for symbol, count_symbol in count_seq.items():
                ## adding link s -> s*t where
                 ## s* is the longest suffix of s
                ## such that s*t is an existing context
                new_seq = list(seq)
                new_seq.append(symbol)
                found_suffix = tuple(_longest_suffix(tuple(new_seq), self.valid_contexts.keys()))
                if p_weight :
                    graph[seq][found_suffix] = count_symbol / supp_s
                else :
                    graph[seq][found_suffix] = count_symbol
        return graph

    def get_networkx_graph(self):
        """Builds a networkx graph from our contexts.

        Returns
        -------
        nx_digraph : DiGraph
            A networkX directional graph with every valid context linking to their next hop
            with the probability to hop.
        """
        graph_dict = self.build_network(False)
        nx_digraph = DiGraph(graph_dict)

        ## compute maximum order among memory nodes
        real_max_order = 0

        for node in nx_digraph.nodes:
            nx_digraph.nodes[node]['item'] = node[-1]
            nx_digraph.nodes[node]['order'] = len(node)
            nx_digraph.nodes[node]['count'] = sum(graph_dict[node].values())
            real_max_order = max(len(node), real_max_order)

        for edge in nx_digraph.edges:
            nx_digraph.edges[edge]['count'] = graph_dict[edge[0]][edge[1]]
            nx_digraph.edges[edge]['weight'] = graph_dict[edge[0]][edge[1]] / nx_digraph.nodes[edge[0]]['count']
        
        nx_digraph.graph['max_order'] = real_max_order
        return nx_digraph

    def get_support(self, context):
        """Returns the given context's support.

        Parameters
        ----------
        context : tuple[str, ...]
            The context to calculate the support from.

        Returns
        -------
        support : int

        """
        return sum(self.count[context].values())

    def get_distribution(self, context):
        """
        Gets the distribution of a certain context

        (Probability of encountering a letter for this context)

        Parameters
        ----------
        context : tuple[str, ...]
            The context to get the distribution from.

        Returns
        -------
        distr : dict[str,float]
            A link between a letter and its probability
            to appear next in the given sequence.
        """

        distr = {}
        count_context = self.count[context]
        support = float(self.get_support(context))
        for target_symbol, target_symbol_count in count_context.items():
            distr[target_symbol] = float(target_symbol_count) / support
        return distr

    def fit(self, sequences):
        """Initialize and fit the data.

        Parameters
        ----------
        sequences : list[list[str]]
            The sequences to fit the data from.

        Returns
        -------
        contexts : defaultdict[tuple[str, ...], dict[str, int]]
            The valid contexts found from the given sequences.

        Notes
        -----
        This function has to be used if anyone wants to use other functions of the class, as it is
        the only function that initialise the class attributes without directly manipulating them.
        """
        self.count = defaultdict(lambda: defaultdict(int))
        self.valid_contexts = defaultdict(dict)
        self.src_to_ext_src = defaultdict(set)
        self.starting_points = defaultdict(set)
        self.sequences = sequences

        self.init_counts()

        ## Retain all contexts of len 1
        ## then resursively look to extend valid contexts
        for source in tuple(self.count.keys()):
            self.retain_context(source)
            self.extend_to_valid_context(source, source)
        return self.valid_contexts

    def get_name(self):
        """Used to be overriden by other models to give their names.

        Raises
        ------
        NotImplementedError
            This function has to be implemented in any inheriting class and this is the parent
            class.
        """
        raise NotImplementedError()

    def get_params_str(self, short=False):
        """Gets the parameters of the current model.

        Parameters
        ----------
        short : bool
            If true, returns a shorter version of the parameters
            (without max_order and min_support).

        Returns
        -------
        params : str
            The parameters, either empty if short is true or the max order and the min support
            otherwise.
        """
        if short:
            return ''
        return f'max_order:{self.max_order};min_support:{self.min_support}'

    def retain_context(self, source):
        """Save 'source' and all of its prefixes into our valid contexts.

        Parameters
        ----------
        source : tuple[str]
            A context to add to our valid contexts
        """
        for order in range(1, len(source)+1):
            seq = source[0:order]
            if not seq in self.count or len(self.count[seq]) == 0:
                self.find_extended_contexts(seq[1:])
            for symbol in self.count[seq]:
                if self.count[seq][symbol] > 0:
                    self.valid_contexts[seq][symbol] = self.count[seq][symbol]

    def init_counts(self):
        """
        Attribute to each letter in each sequences the number of occurrences
        it has in this sequence
        """
        for tindex, trajectory in enumerate(self.sequences):
            for index in range(len(trajectory) - 1):
                source = tuple(trajectory[index:index + 1])
                target = trajectory[index + 1]
                self.count[source][target] += 1
                self.starting_points[source].add((tindex, index))

    def extend_to_valid_context(self, valid, curr):
        """Test if the current context or any of its extensions has a chance of having a relevant 
        extension and save it / them if that is the case.

        Parameters
        ----------
        valid : tuple[str, ...]
            The last valid context the current context extends from.

        curr : tuple[str, ...]
            The current context to extend from.
        """ 
        order = len(curr)      
        if order < self.max_order \
            and self.get_support(curr) >= self.min_support \
            and self.is_ever_valid(valid, curr):
            # Look for possible extensions of context 'curr'
            extensions_curr = self.find_extended_contexts(curr)
            if len(extensions_curr) > 0:
                for ext_curr in extensions_curr:
                    if self.is_context_valid(valid, ext_curr):
                        # 'ext_curr' is a valid extension of context 'valid'
                        self.retain_context(ext_curr)
                        # recursively search for valid extensions
                        # of context 'ext_curr'
                        self.extend_to_valid_context(ext_curr, ext_curr)
                    else:
                        # 'ext_curr' is NOT a valid extension of context 'valid'
                        # recursively search for valid extensions
                        # of context 'valid'
                        self.extend_to_valid_context(valid, ext_curr)

    def find_extended_contexts(self, curr):
        """Finds if extended forms of the current context already exists or not.

        Parameters
        ----------
        curr : tuple[str, ...]
            The context used to check if an extended context of it exists.

        Returns
        -------
        ext_curr : set[tuple[srt, ...]]
            A set containing every extended contexts of the given context.
        """        
        if curr in self.src_to_ext_src:
            return self.src_to_ext_src[curr]
        self.extend_context(curr)
        if curr in self.src_to_ext_src:
            return self.src_to_ext_src[curr]
        return set()

    def extend_context(self, source):
        """Extends the current context if possible and stores it.

        Parameters
        ----------
        source : tuple[str, ...]
            The context to extend from.
        """
        
        if len(source) > 1:
            if (not source[1:] in self.count) \
                or (len(self.count[source]) == 0):
                self.extend_context(source[1:])

        order = len(source)
        temp_count = defaultdict(lambda: defaultdict(int))
        for tindex, index in self.starting_points[source]:
            if index - 1 >= 0 and index + order < len(self.sequences[tindex]):
                ext_source = tuple(self.sequences[tindex][index - 1:index + order])
                target = self.sequences[tindex][index + order]
                temp_count[ext_source][target] += 1
                self.starting_points[ext_source].add((tindex, index - 1))

        if len(temp_count) == 0:
            return
        for seq in temp_count:
            for symbol in temp_count[seq]:
                if temp_count[seq][symbol] < self.min_support:
                    temp_count[seq][symbol] = 0
                self.count[seq][symbol] += temp_count[seq][symbol]
            for symbol in temp_count[seq]:
                if temp_count[seq][symbol] > 0:
                    self.src_to_ext_src[seq[1:]].add(seq)
                    break

    def is_context_valid(self, valid, ext):
        """To be overriden to define what is a valid context in the model.

        Parameters
        ----------
        valid : tuple[str, ...]
            The last valid context ext extends from.

        ext : tuple[str, ...]
            The extension to test the validity from.

        Raises
        ------
        NotImplementedError
            This function has to be implemented in any inheriting class and this is the parent
            class.
        """
        raise NotImplementedError()

    def is_ever_valid(self, valid, curr):
        """
        To be overriden to define if there will ever be a new extension that might be relevent.

        Parameters
        ----------
        valid : tuple[str, ...]
            The last valid context curr extends from.

        curr : tuple[str, ...]
            The current context to test for eventual future validity.

        Raises
        ------
        NotImplementedError
            This function has to be implemented in any inheriting class and this is the parent
            class.
        """
        raise NotImplementedError()
