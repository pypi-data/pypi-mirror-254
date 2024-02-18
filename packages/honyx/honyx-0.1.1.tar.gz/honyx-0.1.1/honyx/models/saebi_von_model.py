"""
Model defining the xu variable order network model as well as some functions
to calculate kullback-leibler divergence
"""


from honyx.models.hon_model import HONModel

from math import log
import sys

######################################################################################
def _kl_divergence(distrib_a, distrib_b):
    """
    Calculate the kullback-leibler divergence between two given distributions.

    Notes
    -----
    See https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence for more
    informations.

    Parameters
    ----------
    distrib_a : dict[str, float]
    distrib_b : dict[str, float]
    """

    res = 0.
    for target, elem_target in distrib_a.items():
        if target in distrib_b:
            res += elem_target * log(elem_target/distrib_b[target], 2)
    return res

######################################################################################
def _kl_divergence_threshold(order, support):
    """
    returns a threshold used with a given α to compare with the kl_divergence

    Parameters
    ----------
    order : int
        The order to calculate the threshold for.
    support : int
        The support to calculate the threshold for.

    Returns
    -------
    threshold : float
        The desired threshold.
    """
    return order / log(1 + support, 2)

######################################################################################
class SaebiVONModel(HONModel):
    """
    Test the validity of an extended context by comparing the Kullback–Leibler divergence
    of the distribution of the extended context and the last valid context
    to a function threshold.
    Parameter alpha is the threshold multiplier (default:1)

    Attributes
    ----------
    alpha : float
        A threshold multiplier.

    References
    ----------
    .. [1] Saebi, Mandana, Jian Xu, Lance M. Kaplan, Bruno Ribeiro, and Nitesh V. Chawla.
      "Efficient modeling of higher-order dependencies in networks:
      from algorithm to application for anomaly detection."
      EPJ Data Science 9, no. 1 (2020): 15.

    .. [2] Jian Xu, Thanuka L. Wickramarathne, and Nitesh V. Chawla.
      "Representing higher-order dependencies in networks."
      Science Advances 2, no. 5 (2016): e1600028.
    """

    def __init__(self, max_order = None, min_support = 1, alpha = 1.):
        """
        Initialise the XuVONModel.
        """
        if max_order is None:
            max_order = sys.maxsize
        HONModel.__init__(self, max_order, min_support)
        self.alpha = alpha

    ######################################################################################
    def get_name(self):
        """
        Overrides to give the model name
        """
        return 'xu'

    ######################################################################################
    def get_params_str(self, short):
        """
        Extends to give the additional alpha parameter
        """
        base_params = super().get_params_str(short)
        return base_params+ f"alpha:{self.alpha}"

    ######################################################################################
    def is_context_valid(self, valid, ext):
        """
        Override to determinate if a context is valid
        """
        supp_ext = sum(x for x in self.count[ext].values())
        ext_distr = self.get_distribution(ext)
        distr_valid = self.get_distribution(valid)
        return _kl_divergence(ext_distr, distr_valid) \
                > self.alpha * _kl_divergence_threshold(len(ext), supp_ext)

    ######################################################################################
    def is_ever_valid(self, valid, curr) -> bool:
        r"""
        Override to determinate if there will ever be a valid extended context from the current one.

        Test whatever the maximum possible KL-divergence of an extension of context 'curr'
        can be greater than the significance threshold. 
        If not, the recurssion looking for relevant contexts should be stopped here.

        Looking for the least likely symbol following context 'valid'
        that is possible to get with 'curr'
        ie looking for min_σ -log_2(P(σ|valid)) st P(σ|curr)>0

        If this quantity is lower than self.alpha * KLDThreshold(order + 1, supp_curr)
        then no valid extention of context 'curr' is possible

        Notes
        -----
        Original code https://github.com/xyjprc/hon/blob/master/pyHON/BuildRulesFastParameterFreeFreq.py

        (Jan 10, 2018 commit) is wrong and uses the quantity
        -log_2(P(σ|valid)) s.t. σ = argmin P(σ|curr)
        i.e. the KLD achieved when (one of) the least likely symbol following 'curr' become the only possible symbol
        note that this quantity is arbitrary as it depends on the way the values are stored in the python dicts.
        We use the equation (1) found in Saebi et al. (2020) i.e.    

        .. math::
        
            \max(\mathcal{D}_{KL}(D_{ext} || D)) \leq -\log_2(\min(P(i)))

        and keep the signiﬁcance threshold used in the original code. We therefore test whether 

        .. math::
            
            -\log_2(\min(P(i))) > \dfrac{k_{curr}+1}{\log_2(1+Support_{S_{curr}})}

        """
        distr_valid = self.get_distribution(valid)
        supp_curr = sum([x for x in self.count[curr].values()])
        return -log(min(distr_valid.values()),2) > self.alpha * _kl_divergence_threshold(len(curr) + 1, supp_curr)
    ######################################################################################
