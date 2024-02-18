# financial_analyzer
[![Documentation Status](https://readthedocs.org/projects/financial-analyzer/badge/?version=latest)](https://financial-analyzer.readthedocs.io/en/latest/?badge=latest)


The `financial_analyzer` package has the goal of helping users solve various finance based problems related to accounting and business operations. The current iteration of the package can be used to understand a business's Cost and Revenue relationships, as well as the Return on Investment. The package implements and easy to use, plug and play parameter ingestion to produce financial results and indicators to help business owners, investors, or members of the financial community.

## Installation and Setup

Financial_Analyzer is still in the development stage and not installable through PyPi. At this moment please follow the developer setup instructions to install and make use of the package.

```bash
$ pip install financial_analyzer
```

### Developer Setup

#### 1. Clone the Repository 
```bash
$ git clone git@github.com:UBC-MDS/financial_analyzer.git
```
Move to this directory in your terminal.

#### 2. Setup the Conda Environment

Create environment for the package:
```bash
conda create -n financial_analyzer python=3.9 -y
```
or
```bash
conda create --name financial_analyzer python=3.9 -y
```
Then active this newly created environment:
```bash
ca financial_analyzer
```


#### 3. Install the Package

```bash
cd dist/
pip install financial_analyzer-0.1.0-py3-none-any.whl
tar xzf financial_analyzer-0.1.0.tar.gz
pip install financial_analyzer-0.1.0/
```
## Test

To test the functions of `financial_analyzer`, open terminal at the directory of `financial_analyzer` package, run below test Commands:

```bash
pip install pytest
pytest tests
```

## Functions 
- `roi(initial_investment, current_value)`: Calculate the return on investment using the initial and current value of investment. 
- `units_for_target_profit(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 200)`: Calculate the number of sold units needed to reach desired profit. 
- `breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit)`: Calculate the break-even point in units (price needed), given a set of cost and revenue parameters. 
- `plot_breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 500)`: Visulize fixed cost, variable cost, and revenue through plotting linear equations. 

## Usage

`financial_analyzer` can be used to calculate and plot an investment's roi and breakeven point as follows: 

```python 
from financial_analyzer.roi import roi
from financial_analyzer.units_for_target_profit import units_for_target_profit
from financial_analyzer.breakeven_point import breakeven_point
from financial_analyzer.plot_breakeven_point import plot_breakeven_point
import plotly.express as px

initial_investment = 400 
current_value = 450
fixed_cost = 1000
sales_price_per_unit = 8 
variable_cost_per_unit = 2 

roi = roi(initial_investment, current_value)
units_tg_profit = units_for_target_profit(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 200)
break_even = breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit)
fig = plot_breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 500)
```

## Python Ecosystem 

`financial_analyzer` possess its focus on answering the commonly needed metrics in finance. The purpose of the package is to allow easy way to access these metrics, and reuse across different files. The `financial_analyzer` is fairly unique in it's application as it does not make use of any other finance based packages to calculate it's metrics and results - however, the package will make use of several statistical and mathematical packages such as `NumPy`, `Pandas`, and `Matplotlib` to produce results for its custom functions. Our package contains a wide array of finance based functions and tools, a similar package is [`ROICalculator`](https://github.com/likeblood/ROICalculator) - at the current version our package is a lot simpler and we hope to work along side their team in the future!

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

The following package was created by the following contributors: Alan Powichrowski, Chris Gao, Nicole T., Rafe Chang.

## License

`financial_analyzer` was created by Nicole Tu, Rafe Chang, Alan PowPowichrowski, Chris Gao. It is licensed under the terms of the MIT license.

## Credits

`financial_analyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
