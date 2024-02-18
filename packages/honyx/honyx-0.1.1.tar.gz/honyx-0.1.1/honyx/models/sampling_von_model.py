"""
Module giving access to the SamplingVONModel or MC-Von
"""

import numpy as np
from scipy.special import comb, loggamma
from math import exp, log, log2
from sys import maxsize

from honyx.models.hon_model import HONModel

from itertools import combinations


######################################################################################
def _kl_divergence_vect(c_p, c_q, n_p, n_q):
    """Compute the kullback divergence  between numpy vectors c_q and c_p

    Parameters
    ----------
    c_p: 1D np-array
    c_q: 1D np-array
    n_p: sum of c_p
    n_q: sum of c_q
    """
    res = 0.
    for i in range(len(c_p)):
        if c_p[i] > 0:
            res += (c_p[i]/n_p)*log2((c_p[i]/n_p)/(c_q[i]/n_q))
    return res
    # return sum(rel_entr(c_p/n_p, c_q/n_q))

######################################################################################
def _fast_binom_pmf(s_n, k, prob):
    """Compute the probability to have k sucess with probability prob among s_n trials 
    using the loggamma function
    
    Parameters
    ----------
    s_n: int
        number of trials
    k: int
        number of sucess
    prob: float [0,1]
        probability of sucess

    Notes
    -----
    see
    `scipy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.loggamma.html#scipy.special.loggamma>`_.
    """
    return exp(loggamma(s_n+1)-loggamma(k+1)-loggamma(s_n-k+1)+k*log(prob)+(s_n-k)*log(1.-prob))

######################################################################################
class SamplingVONModel(HONModel):
    """
    a.k.a. MC-Von model
    A context is considered valid if the p-value of its divergence from the last 
    valid context is less than a given confidence threshold (or here a range)
    The p-value is computed using controlled a Monte-carlo sampling.
    The maximum number of samples is chosen in order to control a given resampling risk ('risk' attribute). 

    Notes
    -----
    Inherit :class:`hon_model.HONModel`

    Attributes
    ----------
    ct_m, ct_p : float, float
        Define a lower and upper significance thresholds used to verify validity.
    risk: float
        in [0,1]. The resampling risk
    method: str ['marginals', 'count']
        method used for multivariate_hypergeometric draws
    nmax: int
        Maximum number of sample used to compute the p-value
    seed: int
        Seed to initialize the random number generator (numpy.random.default_rng)
    """
    def __init__(self, max_order=None, min_support=1, ct_m=0.001, ct_p=0.0015, risk = 0.01, method='marginals', nmax = 40000, seed = None):
        if max_order is None:
            max_order = maxsize
        HONModel.__init__(self, max_order, min_support)
        assert ct_m < ct_p, 'Error: ct_m param should be lower than ct_p'
        self.ct_m = ct_m
        self.ct_p = ct_p
        self.risk = risk
        self.method = method
        ## find p such that B(n, α^-, np) = B(n, α^+, np)
        self.ct_crit = log((1.-self.ct_p)/(1.-self.ct_m))/(log((1.-self.ct_p)/self.ct_p) - log((1.-self.ct_m)/self.ct_m))
        self.lim_nb_draws = self.max_nb_draws()
        if nmax is not None:
            self.lim_nb_draws = min(self.lim_nb_draws, nmax)
        self.rng_gen =  np.random.default_rng(seed)

    ######################################################################################
    def get_name(self):
        """Overrides to give the name of this model."""
        return "samp"

    ######################################################################################
    def get_params_str(self, short=False):
        """Extends to show the extra information in the model (which is pval)."""
        base_params = super().get_params_str(short)
        return (base_params+ f"ct_m:{self.ct_m};ct_p:{self.ct_p};risk:{self.risk};max_draws:{self.lim_nb_draws}")
    
    ######################################################################################
    def max_nb_draws(self):
        ## find n such that (n+1) * min(B(n, α^-, np*), B(n, α^+, np*)) <=  ϵ
        inc = 100000
        max_n = 0
        while inc >= 1:
            for k in range(1,11):
                i = max_n + k*inc
                if (i+1.)*min(_fast_binom_pmf(i, i*self.ct_crit, self.ct_p), _fast_binom_pmf(i, i*self.ct_crit,self.ct_m)) <= self.risk:
                    break
            max_n = i - inc
            inc = int(inc/10)
        return max_n

    ######################################################################################
    def is_valid_csm(self, c_val, n_e, kld):
        """Performs a controlled Monte-Carlo Sampling to test whether the value kld could 
        have been obtained by ramdomly sampling n_e elments from the vector c_val."""
        n_v = np.sum(c_val)
        Sn = 0
        i=1
        for draw in self.rng_gen.multivariate_hypergeometric(c_val, n_e, size=self.lim_nb_draws, method=self.method):
            kld_t = _kl_divergence_vect(draw, c_val, n_e, n_v)
            if kld_t >= kld:
                Sn += 1
            if i >= 10 :   
                Bm = (i+1.)*_fast_binom_pmf(i, Sn, self.ct_m)                       
                Bp = (i+1.)*_fast_binom_pmf(i, Sn, self.ct_p)
                if min(Bm, Bp) <= self.risk:
                    # return Bp <= Bm
                    break
            i += 1
        return Sn / i <= self.ct_crit

    ######################################################################################
    def is_context_valid(self, valid, ext):
        """Overrides to determinate if the given context is valid or not for this model."""

        dict_val = self.count[valid]
        dict_ext = self.count[ext]

        c_val, c_ext = np.zeros(len(dict_val), dtype=int), np.zeros(len(dict_val), dtype=int)
        index = 0
        for key, val in dict_val.items():
            c_val[index] = val            
            if key in dict_ext:
                c_ext[index] = dict_ext[key]
            index += 1

        k = len(c_val)
        n_v = int(np.sum(c_val))
        n_e = int(np.sum(c_ext))

        assert n_e > 0, 'Error: no obs. of extended context.'

        ## Test trivial cases
        if n_v <= 1 or k == 1 or n_e == n_v or np.max(c_val)==1 or 1./ comb(n_v, n_e) > self.ct_m:
            return False

        ext_kld = _kl_divergence_vect(c_ext, c_val, n_e, n_v)
        
        return self.is_valid_csm(c_val, n_e, ext_kld)

    ######################################################################################

    def is_ever_valid(self, valid, curr):
        """Overrides to determinate if the given context can have a valid extension
        for this model."""
        n_v = sum(self.count[valid].values())
        n_c = sum(self.count[curr].values())
        if n_v > n_c:
            max_comb_nc = int(n_v / 2) if n_c > int(n_v / 2) else n_c
            return self.ct_m >= 1./ comb(n_v, max_comb_nc)
        return True

    ######################################################################################
