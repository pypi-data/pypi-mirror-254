def roi(initial_investment, current_value):
    """ Calculate the Return on Investment (ROI).
    
    Parameters 
    ----------
    initial_investment : {float, int} 
        The initial amount invested.
    current_value : {float, int}  
        The current value of the investment.
    
    Returns
    --------
    float: The ROI expressed as a percentage.
    
    Examples 
    --------
    Context: You are selling paintings, your initial investment is 1,000,000 dollars. 2 months later, the value of your initial investment grew to 1,200,000 dollars, what is your return on investment? 
    >>> initial_investment = 1000000
    >>> current_value = 1200000
    >>> roi = roi(initial_investment, current_value)
    >>> print(f"The roi of your ivestment is {roi} %")
    The roi of your ivestment is 20%
    """
    
    #Check data type
    if any(not isinstance(param, (float, int)) for param in [initial_investment, current_value]):
        raise TypeError("All parameters must be of type float or int.")

    #Check value
    if initial_investment < 0:
        raise ValueError("Initial investment should be positive!")
    
    return ((current_value - initial_investment) / initial_investment) * 100

