import altair as alt
import numpy as np
import pandas as pd

def plot_breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit, max_units):
    """
    Plot a break-even point graph which shows the relationship between total cost,
    total revenue, and number of units sold. This plot will include 3 lines, one for
    Total Revenue, one for Total Cost (Varialbe + Fixed), and one for Fixed Cost.

    Parameters
    ----------
    fixed_costs : float
        Total fixed costs in the problem, given as a float.
    sales_price_per_unit : float
        The selling price of each unit in the problem, given as a float.
    variable_cost_per_unit : float
        The variable cost of each unit in the problem, given as a float.
    max_units : int
        The maximum number of units to include in the plot, given as an integer.

    Returns
    -------
    None
        This function does not return a value. It displays a plot.

    Examples
    --------
    Context: Want to visualize cafe sales. Your fixed costs are $1,000, each coffee 
    sells for $5, the variable cost for each cup is $2. To visualize (altair plot) 
    your costs and revenue up to selling 500 cups, you use this function.
    
    >>> fixed_costs = 1000
    >>> sales_price_per_unit = 5
    >>> variable_cost_per_unit = 2
    >>> max_units = 500
    >>> plot_breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit, max_units)
    
    This will display an altair plot with the total cost, fixed cost, and total revenue lines, 
    illustrating the point where they intersect as the break-even point.
    """
    unit_range_x = np.arange(1, max_units+1)

    plot_df = pd.DataFrame({
      'Units': unit_range_x,
      'Total Revenue': unit_range_x * sales_price_per_unit,
      'Total Cost': fixed_costs + variable_cost_per_unit * unit_range_x,
      'Fixed Cost': np.ones(max_units)*fixed_costs,
      'Total Variable Cost': unit_range_x * variable_cost_per_unit})
    
    total_rev_chart = alt.Chart(plot_df).mark_line().encode(
    x='Units',
    y='Total Revenue',
    color= alt.value("green")).properties(
    width=600,
    height=400)

    total_cost_chart = alt.Chart(plot_df).mark_line().encode(
    x='Units',
    y='Total Cost',
    color=alt.value('red')).properties(
    width=600,
    height=400)

    fixed_cost_chart = alt.Chart(plot_df).mark_line().encode(
    x='Units',
    y='Fixed Cost',
    color=alt.value('orange')).properties(
    width=600,
    height=400)

    title_legend = alt.Chart({'values':[{}]}).mark_text(
        align='left', dx=600, dy=-5, text='Legend:', color='black'
    ).encode(
        x=alt.value(20),  # pixels from left
        y=alt.value(20))   # pixels from top
    
    rev_legend = alt.Chart({'values':[{}]}).mark_text(
        align='left', dx=600, dy=-5, text='Total Revenue', color='green'
    ).encode(
        x=alt.value(20),  # pixels from left
        y=alt.value(40))   # pixels from top

    cost_legend = alt.Chart({'values':[{}]}).mark_text(
        align='left', dx=600, dy=-5, text='Total Cost', color='red'
    ).encode(
        x=alt.value(20),  # pixels from left
        y=alt.value(60))   # pixels from top
    
    fixed_cost_legend = alt.Chart({'values':[{}]}).mark_text(
        align='left', dx=600, dy=-5, text='Fixed Cost', color='orange'
    ).encode(
        x=alt.value(20),  # pixels from left
        y=alt.value(80))   # pixels from top
    
    break_even_units = fixed_costs / (sales_price_per_unit - variable_cost_per_unit)
    break_even_revenue = break_even_units * sales_price_per_unit

    break_even_point = alt.Chart(pd.DataFrame(
        {'Units': [break_even_units], 'Total Revenue': [break_even_revenue]}
        )).mark_point(
            color='blue', size=100).encode(
                x='Units', y='Total Revenue')
    
    be_point_legend = alt.Chart({'values':[{}]}).mark_text(
        align='left', dx=600, dy=-5, text='Break Even Point', color='blue'
    ).encode(
        x=alt.value(20),  # pixels from left
        y=alt.value(100))   # pixels from top
    
    # Combining the charts with legends
    chart = (total_rev_chart + total_cost_chart + fixed_cost_chart +
             title_legend + rev_legend + cost_legend + fixed_cost_legend +
            break_even_point + be_point_legend)
    
    return chart, plot_df