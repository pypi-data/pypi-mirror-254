"""
Module to define the FixOrderModel, to create a fixed-order network.
"""

from honyx.models.hon_model import HONModel

class FixOrderModel(HONModel):
    """
    Model where every existing subsequence of length <= maxOrder
    is a valid context.

    Notes
    -----
    Can result in a very large object for higher maxOrder and
    sequences on a large number of items.

    Same attributes as :class:`hon_model.HONModel`.
    """

    ######################################################################################
    def __init__(self, max_order, min_support = 1):
        HONModel.__init__(self, max_order, min_support)

    ######################################################################################
    def is_context_valid(self, valid, ext):
        """
        Overrides to return true if we are under or equal maxOrder and we haven't 
        gone under the min_support.

        Notes
        -----
        The model is a fix-order model, thus, every context that is under or equal to the 
        max_support and that isn't less than the min_support is considered to be valid.

        Parameters
        ----------
        valid : tuple[str, ...]
            The last valid context ext extends from.
        ext : tuple[str, ...]
            The context to test for validity.
        order : int, default = 0
            The order of the tested context

        Returns
        -------
        validity : bool
            Whether the test context is valid or not.
        """

        order = len(ext)
        if order > self.max_order:
            return False
        if sum(self.count[ext].values()) < self.min_support:
            return False
        return True
	######################################################################################
    def is_ever_valid(self, valid, curr, order=0):
        """
        Returns true if we aren't above the max order.

        Notes
        -----
        As the fix-order model is straightforward, we can know if an extension of the current 
        context will be valid simply by knowing if the current context is 
        lesser or equal to the max_order.

        Returns
        -------
        ever_valid : bool
            The current context has eventual valid extensions.
        """

        return order <= self.max_order
	######################################################################################
    def get_general_name(self):
        """Overrides to return the general name of the current FON without its max order.

        Returns
        -------
        name : str
            The name of the model.
        """

        return 'fon'
	######################################################################################
    def get_name(self):
        """Return the specific name of the current FON with its max order.

        Returns
        -------
        name : str
            The name of the model with the max order.
        """
        return f'fon_{self.max_order}'
