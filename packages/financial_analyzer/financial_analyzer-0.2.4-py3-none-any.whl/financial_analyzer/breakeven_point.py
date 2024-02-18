def breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit):
    """
    Calculate the break-even point in units, with given set of cost and revenue parameters.

    Parameters
    ----------
    fixed_costs : float 
        Total fixed costs in the problem, given as a float.
    sales_price_per_unit : float
        The selling price of each unit in the problem, given as a float.
    variable_cost_per_unit : float
        The variable cost of each unit in the problem, given as a float.

    Returns
    -------
    float
        The break-even point in units for the given parameters.

    Examples
    --------
    Context: You are selling paintings, your fixed costs are 
    $5,000/month, each painting is sold for $20, the variable 
    costs (materials) for each painting are $10. What is your 
    break even point?
    >>> fixed_costs = 5000
    >>> sales_price_per_unit = 20
    >>> variable_cost_per_unit = 10
    >>> break_even_units = breakeven_point(fixed_costs, 
    >>>     sales_price_per_unit, 
    >>>     variable_cost_per_unit)
    >>> print(break_even_units)
    500
    """

    #Check type is correct
    for param in [fixed_costs, sales_price_per_unit, variable_cost_per_unit]:
        if not isinstance(param, (float, int)):
            raise TypeError("All parameters must be of type float or int.")

    #Check value is positive
    if fixed_costs < 0 or sales_price_per_unit < 0 or variable_cost_per_unit < 0:
        raise ValueError("All parameters must be non-negative.")

    #Check to avoid ZeroDivision error
    if sales_price_per_unit <= variable_cost_per_unit:
        raise ZeroDivisionError("Sales price per unit must be greater than variable cost per unit.")
    
    return fixed_costs / (sales_price_per_unit - variable_cost_per_unit)
