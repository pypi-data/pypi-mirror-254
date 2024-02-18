from honyx import models

__all__ = ["generate_hon",
           "read_sequences"]


_models = {"fix-order": models.fix_order_model.FixOrderModel, 
           "optimal-order": models.optimal_order_model.OptimalOrderModel,
           "variable-order": models.saebi_von_model.SaebiVONModel,
           "variable-order-samp": models.sampling_von_model.SamplingVONModel}

def read_sequences(path,
                   comments="#",
                   delimiter=",",
                   remove_rep=False,
                   itemtype=None):
    """
    Read a sequence dataset from a file.

    Parameters
    ----------
    path : string
       Filename to read.
    comments : string, optional
       The character used to indicate the start of a comment. To specify that
       no character should be treated as a comment, use ``comments=None``.
    delimiter : string, optional
       The string used to separate values.  The default is a comma.
    itemtype : int, float, str, Python type, optional
        Convert node data from strings to specified type

    Returns
    -------
    sequences : list of lists [itemtype]
        The sequences read from the file
        
    Raises:
    -------
    TypeError
        if items in file cannot be converted to given itemtype

    """
    sequences = []
    
    with open(path, 'r') as file:
        for line in file:
            if comments is not None:
                p = line.find(comments)
                if p >= 0:
                    line = line[:p]
                if not line:
                    continue
            s = line.strip().split(delimiter)
            if len(s) < 2:
                continue
            seq = []
            if itemtype is not None:
                try:
                    seq = [itemtype(item) for item in s]
                except Exception as err:
                    raise TypeError(
                        f"Failed to convert items in seq to type {itemtype}."
                    ) from err
            else:
                seq = s
            sequences.append(seq)
    if remove_rep:
        nsequences = []
        for index_seq in range(len(sequences)):
            seq = sequences[index_seq]
            nseq = []
            for s in seq:
                if len(nseq) == 0 or s != nseq[-1]:
                    nseq.append(s)
		    ## sequences of length 1 are useless for us
            if len(nseq) > 1:
                nsequences.append(nseq)
        return nsequences
    return sequences

def generate_hon(sequences, model, **kwargs):
    """
    Generate a Higher-order network using the input sequences dataset 
    according to specified HON model.

    Available models (and their parameters) are:
        - fix-order (max_order: int, min_support: int). 
        Fixed-order model contaings all memory nodes of order <= max_order

        - optimal-order (max_order: int, min_support: int, ct: float ]0,1]). 
        Find the best maximum order up to max_order with a threshold ct on the p-value.

        - variable-order (max_order: int, min_support: int, alpha: float > 0). 
        Variable-order network where memory-nodes are added if the divergence between following items is above a function threshold
        
        - variable-order-samp (max_order: int, min_support: int, ct_m: float ]0,1], ct_p: float ]0,1], risk: float ]0,1])

    See documentation for further details about the HON models. 

    The graph has the following attributes:
        - Graph *max_order* (int) 
          Maximum order (length) of memory-nodes in G 

        - Node *item* (str)
          The original item represented by this memory-node
            
        - Node *count* (int)
          Number of occurences of the corresponding subsequences in the dataset
          (excluding occurences where the subsequence is at the end of a sequence)

        - Edge *count* (int)
          For a link ABC -> D, number of occurence of "ABCD" in the dataset

        - Edge *weight* (float)
          For a link ABC -> D, probability of transition for ABC to D


    Parameters
    ----------
    sequences : list[list[str]]
        dataset of sequences
    
    model : str
        the model used to build the network
    
    kwargs : 
        additionnal parameter for the HON model (see above)

    Returns
    -------
    G : NetworkX digraph
        The constructed Higher-order network.
        
    Raises:
    -------
    ValueError
        if the model parameter is not an available model

    Examples
    --------
    >>> import honyx
    >>> sequences = [['a','b','r','a','c','a','d','a','b','r','a']]
    >>> honyx.generate_hon(sequences, "fix-order", max_order = 1, min_support = 1)
    DiGraph with 5 nodes and 7 edges
    >>> honyx.generate_hon(sequences, "fix-order", max_order = 2, min_support = 1)
    DiGraph with 12 nodes and 14 edges
    >>> honyx.generate_hon(sequences, "variable-order", max_order = 3)
    DiGraph with 5 nodes and 7 edges
    
    """
    if model not in _models.keys():
        raise ValueError(f'{model} is not an available HON model.\n Available models: {", ".join(_models.keys())}')
    hon_model = _models[model](**kwargs)
    hon_model.fit(sequences)
    return hon_model.get_networkx_graph()