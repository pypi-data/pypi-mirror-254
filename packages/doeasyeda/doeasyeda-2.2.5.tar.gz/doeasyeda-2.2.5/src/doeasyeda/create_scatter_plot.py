import altair as alt

# Define custom error handling
class DoEasyEDAException(Exception):
    def __init__(self, message, original_exception):
        super().__init__(f"{message}: {original_exception}")
        self.original_exception = original_exception


def create_scatter_plot(df, x_col, y_col, size=60, color=None, title=None,
                        x_title=None, y_title=None, tooltip=None,
                        interactive=False, width=None, height=None):
    """
    Creates a scatter plot using Altair with customizable options.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing the data for the scatter plot.
    x_col : str
        The column name to be used for the x-axis.
    y_col : str
        The column name to be used for the y-axis.
    size : int, optional
        The size of the scatter plot markers (default is 60).
    color : str, optional
        The column name to be used for color encoding (default is None).
    title : str, optional
        The title of the scatter plot (default is None).
    x_title : str, optional
        The title for the x-axis (default is None).
    y_title : str, optional
        The title for the y-axis (default is None).
    tooltip : list of str, optional
        List of column names to be used for tooltips (default is None).
    interactive : bool, optional
        If True, enables interactive features like zooming and panning (default is False).
    width : int, optional
        The width of the chart (default is None).
    height : int, optional
        The height of the chart (default is None).

    Returns
    -------
    alt.Chart
        An Altair Chart object representing the scatter plot.

    Example
    -------
    >>> data = pd.DataFrame({'gdpPercap': [1000, 2000, 3000, 4000],
    ...                      'lifeExp': [70, 80, 60, 65],
    ...                      'continent': ['Asia', 'Europe', 'Africa', 'Americas']})
    >>> create_scatter_plot(data, 'gdpPercap', 'lifeExp', size=60, color='continent',
    ...                     title='Life Expectancy vs GDP Per Capita by Continent',
    ...                     x_title='GDP Per Capita', y_title='Life Expectancy', interactive=True)
    """

    # Validate dataframe
    if df.empty:
        raise ValueError("Empty dataframe received!")

    # Validate input columns x_col, y_col, tooltip
    for col in [x_col, y_col] \
        + ([color] if color else []) \
        + (tooltip if isinstance(tooltip, list) else [tooltip] if tooltip else []):
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in dataframe!")

    # More checking can be added here

    try:
        # Set Altair base chart
        chart = alt.Chart(df).mark_circle(size=size)

        # Set Altair encoding with optional color and tooltip
        encoding = {
            'x': alt.X(x_col, title=x_title),
            'y': alt.Y(y_col, title=y_title)
        }
        if color:
            encoding['color'] = color
        if tooltip:
            encoding['tooltip'] = tooltip if isinstance(tooltip, list) else [tooltip]
    
        # Pass the encoding to chart
        chart = chart.encode(**encoding)
    
        # Set optional title, interactive, width and height
        if title:
            chart = chart.properties(title=title)
        if interactive:
            chart = chart.interactive()
        if width and height:
            chart = chart.properties(width=width, height=height)
        
        return chart

    except Exception as e:
        # Error Handling
        raise DoEasyEDAException("Error in creating scatter plot", e)
