from math import log


__all__ = ["predict",
           "likelihood", 
           "seq_likelihood"]

def predict(G, context):
        """
        Returns the probabilities associated with the specified context

        Parameters
        ----------
        G: DiGraph
            A Higher-Order Network (Networkx' Digraph)

        context : list or tuple of str
            sequence of previsouly visited items

        Returns
        -------
        probas : dict[str]->float
            The probability of appearance of  each item after the specified context

        Notes
        -----
        This function looks for the memory-nodes who is the longest suffix of 'context'
        in G and outputs the transition probabilities for each following item
        """

        if len(context) < 1:
            raise ValueError("Input context is empty")
        
        t_con = tuple(context)
        max_order = G.graph['max_order']
        if len(context) > max_order:
            t_con = tuple(context[:-max_order])
        m_node = None
        while m_node == None and len(t_con) > 0:
            for n in G.nodes:
                if n == t_con:
                    m_node = n
                    break
            t_con = t_con[1:]

        if len(t_con) == 0 and m_node == None:
            raise ValueError(f'Item in {context} not seen during HON construction')
        
        probs = {}
        for _, v, data in G.out_edges(m_node, data=True):
            probs[v[-1]] = data['weight']
        return probs

def likelihood(G, sequences, return_log=False, return_sum=False):
    '''
    Return the average probability that a random walker produce the specified 
    sequences on the higher-order network G

    Parameters
    ----------
    G: DiGraph
        A Higher-Order Network (Networkx' Digraph)
    seq: list of list or list of str
        list of sequences of item
    return_log: bool, optional (default=False)
        if true return the log likelihood (no effect if parameters return_sum=True)
    return_sum: bool, optional (default=False)
        if true return the sum of transitition probabilities

    Returns
    -------
    likelihood: float
        Average probability that a random walker 
    '''
    likelihood = 0.
    if not return_log and not return_sum:
        likelihood = 1.
    nbseq_length_up2 = 0.
    for seq in sequences:
        if len(seq) > 1:
            nbseq_length_up2 += 1
            seq_l = seq_likelihood(G, seq, return_log, return_sum)
            if not return_log and not return_sum:
                likelihood *= seq_l
            else:
                if return_sum:
                    likelihood += seq_l / (len(seq) - 1.)
                else:
                    likelihood += seq_l
    if return_sum:
        likelihood /= nbseq_length_up2
    return likelihood 

def seq_likelihood(G, seq, return_log=False, return_sum=False):
    '''
    Returns the probability that a random walker produce the specified 
    sequence of items on the higher-order network G

    Parameters
    ----------
    G: DiGraph
        A Higher-Order Network (Networkx' Digraph)
    seq: tuple or list of str
        sequence of item
    return_log: bool, optional (default=False)
        if true return the log likelihood (no effect if parameters return_sum=True)
    return_sum: bool, optional (default=False)
        if true return the sum of transitition probabilities

    Returns
    -------
    likelihood: float
        Probability that a random walker produces the specified sequence of item 
    '''
    likelihood = 0.
    if not return_log and not return_sum:
        likelihood = 1.
    ## get first node
    cur_node = None
    for n, data in G.nodes(data=True):
        if data['order']==1 and data['item']==seq[0]:
            cur_node = n
            break
    if cur_node is None:
        # raise ValueError(f'{seq[0]} not in the alphabet used to build HON.')
        return 0.
	
    for i in range(1, len(seq)):
        next_node = None
        next_p = 0.
        for _, v, data in G.out_edges(cur_node, data=True):
            if v[-1] == seq[i]:
                next_node = v 
                next_p = data['weight']
                break
        cur_node = next_node
        if return_sum:
            if cur_node == None:
                for n, data in G.nodes(data=True):
                    if data['order']==1 and data['item']==seq[i]:
                        cur_node = n
                        break
                if cur_node is None:
                    # raise ValueError(f'{seq[i]} not in the alphabet used to build HON.')
                    continue
            else:
                likelihood += next_p
        else:
            if cur_node == None:
                likelihood = 0.
                break
            if return_log:
                likelihood -= log(next_p)
            else:
                likelihood *= next_p
    return likelihood



        

