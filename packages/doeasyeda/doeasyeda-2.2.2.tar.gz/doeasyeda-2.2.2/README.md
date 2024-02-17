# doeasyeda

<figure>
    <img src="https://github.com/UBC-MDS/doeasyeda/blob/main/img/logo2.png?raw=true" alt="Alt text for image" width="200" height="200">
</figure>

[![ci-cd](https://github.com/UBC-MDS/doeasyeda/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/doeasyeda/actions/workflows/ci-cd.yml) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) [![codecov](https://codecov.io/gh/UBC-MDS/doeasyeda/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/doeasyeda) [![Documentation Status](https://readthedocs.org/projects/stock_analyzer/badge/?version=latest)](https://doeasyeda.readthedocs.io/en/latest/?badge=latest) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/github/v/release/UBC-MDS/doeasyeda) ![release](https://img.shields.io/github/release-date/UBC-MDS/doeasyeda)

**doeasyeda** 
---------------------------------------------------------------------------------------

[Installation](#Installation) | [Functions](#Functions) | [Why doeasyeda](#Why-doeasyeda) | [Usage](#Usage)

---

## Project Summary

**doeasyeda** is a Python package designed to streamline the process of Exploratory Data Analysis (EDA) by providing a suite of functions specifically tailored for creating standard EDA plots. This package aims to simplify the visualization aspect of data analysis, making it more accessible and efficient for users.

## Contributors

[Riya Eliza](https://github.com/riyaeliza123), UBC-MDS [✉️](mailto:riya2023@student.ubc.ca)

[Hina Bandukwala](https://github.com/hbandukw),  UBC-MDS [✉️](mailto:hinab@student.ubc.ca)

[Dan Zhang](https://github.com/wqxxzd), UBC-MDS [✉️](mailto:wqxxzd@student.ubc.ca)

[Doris Wang](https://github.com/MDSFusionist), UBC-MDS [✉️](mailto:doris531@student.ubc.ca)

## Installation

```bash
$ pip install doeasyeda
```

## Package Content

This package offers four primary functions, each harnessing the power of the Altair visualization library to create distinct types of plots. These functions provide extensive customization options to cater to diverse data visualization needs.

### Functions:

This package includes four main function:

1. `create_scatter_plot(df, x_col, y_col, size=60, color=None, title=None, x_title=None, y_title=None, tooltip=None, interactive=False, width=None, height=None)`: Generates a scatter plot using the Altair visualization library with various customization options.
2. `create_hist_plot(df, x_col, y_col, color=None, title=None, x_title=None, y_title=None, tooltip=None, interactive=False, width=None, height=None)`: Generates histogram using the Altair visualization library with various customization options.
3. `create_line_plot(df, x_col, y_col, size=1, color=None, title=None, x_title=None, y_title=None, tooltip=None, interactive=False, width=None, height=None)`: Generates a line plot using the Altair visualization library with various customization options.
4. `create_area_plot(df, x_col, y_col, color=None, title=None, x_title=None, y_title=None, tooltip=None, interactive=False, width=None, height=None)`: Generates an area plot using the Altair visualization library with various customization options.

### Common Parameters:

* `df` (pd.DataFrame): The DataFrame containing the data for visualization.
* `x_col`, `y_col` (str): Names of the columns to be used for the x and y axes, respectively.
* `color` (str, optional): Column name for color encoding, defaults to `None`.
* `size` (int, optional): Marker size, default 60.
* `title`, `x_title`, `y_title` (str, optional): Titles for the plot and axes, default `None`.
* `tooltip` (list of str, optional): List of column names for tooltips, defaults to `None`.
* `interactive` (bool, optional): If `True`, enables interactive features such as zooming and panning, defaults to `False`.
* `width`, `height` (int, optional): Dimensions of the chart, defaults to `None`.

## Why doeasyeda?

**doeasyeda** positions itself as a valuable addition to the Python ecosystem, particularly in the realm of data visualization and EDA. While it shares its fundamental objective with existing packages like [pandas-profiling](https://github.com/ydataai/ydata-profiling) and [Dtale](https://pypi.org/project/dtale/), which provides comprehensive EDA reports with a single line of code, **doeasyeda** differentiates itself by focusing on customizable, individual plot generation. While pandas-profing is excellent for generating automated detailed reports on entire datasets, Dtale integrates advanced libraries like Plotly and Seaborn , **doeasyeda** allows users more control and flexibility in visualizing specific aspects of their data through its range of plotting functions from [altair ](https://altair-viz.github.io/index.html)library. Compared to altair, **doeasyeda** has the following key features:

* **Streamlined Simplicity** : `doeasyeda` stands out with its intuitive design, offering a user-friendly alternative to more complex packages like Altair. It enables users to produce comprehensive plots through straightforward, one-liner functions, making the transition from data to insights both efficient and effortless.
* **Tailored for EDA Efficiency** : Unlike the broad-spectrum approach of Altair, `doeasyeda` hones in on the essential plots used in EDA, providing a curated set of tools that streamline the visualization process. This dedicated focus allows for quick generation of standard EDA plots, facilitating a more efficient analysis workflow without the overhead of more intricate coding structures.

## Developer Note

Direct to the root of the project repository

1. To create a new virtual environment in Conda with Python, use the following commands in the terminal :

```
$ conda create --name doeasyeda python=3.9.0 -y
```

2. To use this new environment for developing, we need to activate the virtual environment:

```
$ conda activate doeasyeda
```

3. To install the needed packages via poetry, run the following command. If poetry hasn't been set up yet, please following [this link](https://python-poetry.org/docs/) for installtion.

```
$ poetry install
```

4. To test the package, please run the following command
```
$ pytest tests/
$ pytest tests/ --cov=doeasyeda --cov-report=xml
```

5. The set up is done, you are free to use the doeasyeda package now! Please check the function section above on how to use the package.

## Usage

Our package primarily utilizes the gapminder dataset to demonstrate the effectiveness and versatility of our plotting functions. However, the functions within **doeasyeda** are designed to be flexible and can be applied to a wide range of datasets, making this package a valuable tool for any data scientist or analyst looking to conduct comprehensive EDA.

Below is a simple quick start example:

```
import pandas as pd

from doeasyeda.create_scatter_plot import create_scatter_plot
from doeasyeda.create_line_plot import create_line_plot
from doeasyeda.create_hist_plot import create_hist_plot
from doeasyeda.create_area_plot import create_area_plot

df = pd.read_csv('gapminder.csv')
```

**Creating scatter plot:**

```
create_scatter_plot(df, 'continent', 'lifeExp', color='continent', 
                    title='Life Exp by Continent', x_title= 'Continent', y_title='Life Exp')
```

<img src="https://github.com/UBC-MDS/doeasyeda/blob/main/img/scatterplot.png?raw=true" height="300">

**Creating histogram:**

```
df_grouped1 = df.groupby(['continent'])['lifeExp'].sum().reset_index()
create_hist_plot(df_grouped1, 'continent', 'lifeExp', color='continent', 
                 title='Average Life Exp by Continent', x_title= 'Continent', y_title='Average Life Exp')
```

<img src="https://github.com/UBC-MDS/doeasyeda/blob/main/img/histplot.png?raw=true" height="300">

**Creating area plot:**

```
df_grouped2 = df.groupby(['continent', 'year'])['population'].sum().reset_index()
create_area_plot(df_grouped2, 'year', 'population', color='continent', 
                 title='Total Population by Continent', x_title= 'Continent', y_title='Total Population')
```

<img src="https://github.com/UBC-MDS/doeasyeda/blob/main/img/areaplot.png?raw=true" height="300">

**Creating line plot:**

```
df['gdp'] = df['gdpPercap'] * df['population']
df_grouped3 = df.groupby(['continent', 'year'])[['population', 'gdp']].sum().reset_index()
df_grouped3['gdpPercap'] = df_grouped3['gdp']/df_grouped3['population']
create_line_plot(df_grouped3, 'year', 'gdpPercap', color='continent', 
                 title=' GDP per capita by Continent', x_title= 'Continent', y_title='GDP per capita')
```

<img src="https://github.com/UBC-MDS/doeasyeda/blob/main/img/lineplot.png?raw=true" height="300">

## Documentation

Online documentation can be found [here](https://doeasyeda.readthedocs.io/en/latest/?badge=latest).

Publishing on [TestPyPi]() and [PyPi]() (forthcoming)).

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`doeasyeda` was created by Riya Eliza, Hina Bandukwala, Dan Zhang and Doris Wang. It is licensed under the terms of the MIT license.

## Credits

`doeasyeda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Reference

Jacob VanderPlas, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, & Scott Sievert (2018). Altair: Interactive Statistical Visualizations for Python*. Journal of Open Source Software,  *3* (32), 1057.

*Simon Brugman. (2019). ydata-profiling: Exploratory Data Analysis for Python. .

dtale · PyPI. https://pypi.org/project/dtale/

*Download the data | Gapminder* . (n.d.). Retrieved from https://www.gapminder.org/data/
