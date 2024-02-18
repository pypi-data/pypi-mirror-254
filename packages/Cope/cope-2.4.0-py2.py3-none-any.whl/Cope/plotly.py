"""
Functions & classes that extend the plotly library
"""

try:
    import polars as pl
    import numpy as np
    import plotly.graph_objects as go
except: pass
else:
    # Tested manually elsewhere
    # TODO: add manual tests here
    def ridgeplot(df:pl.DataFrame, x:str, y:str=None, z:str=None, dist:float=.5, overlap:float=0, **kwargs) -> go.Figure:
        """ Create a ridgeplot in plotly.
            `x` is the name of the column in `df` that specifies the x data.
            `y` can either be the name of the column of the y axis data, if `df` is in
                long format, or left unspecified if `df` is in wide format. If in wide
                format, it's implied that the data in the columns specified by `z` are
                the y data.
            `z` is either a list of columns of `y` data (the column names are then `z`)
                if `df` is in wide format, or the column name in `df` of the labels
                that say what each sample belongs to, if in long format.
            `dist` dictates how close each `z` is. 0 means the max value of each `z`
                is the min value of the one above it, and 1 means the min value of each
                `z` is the start of the shading of the `z` above it. Increasing this
                also makes each `z` taller to compensate.
            `overlap` effects the size of the shading directly. Usually between -1
                and 1.
        """
        # The idea behind this ridgeline plot with Plotly is to add traces manually
        assert z is not None
        # Cast to polars, in case pandas was given
        df = pl.DataFrame(df)

        if y is None:
            assert isinstance(z, (tuple, list))
            zs = z
        else:
            zs = df[z].unique()

        array_dict = {} # instantiating an empty dictionnary
        if y is None:
            for i in z:
                array_dict[f'x_{i}'] = df[x]
                # we normalize the array (min max normalization)
                array_dict[f'y_{i}'] = df[i]
                array_dict[f'y_{i}'] = (array_dict[f'y_{i}'] - array_dict[f'y_{i}'].min()) / (array_dict[f'y_{i}'].max() - array_dict[f'y_{i}'].min())
        else:
            for i in df[z].unique():
                array_dict[f'x_{i}'] = df.filter(pl.col(z) == i)[x]
                # we normalize the array (min max normalization)
                array_dict[f'y_{i}'] = df.filter(pl.col(z) == i)[y]
                array_dict[f'y_{i}'] = (array_dict[f'y_{i}'] - array_dict[f'y_{i}'].min()) / (array_dict[f'y_{i}'].max() - array_dict[f'y_{i}'].min())

        # once all of this is done, we can create a plotly.graph_objects.Figure and add traces with fig.add_trace() method
        # since we have stored the values and their respective x for each z, we can plot scatterplots (go.Scatter)
        # we thus iterate over the z's and create a 'blank line' that is placed at y = index, then the corresponding x line
        fig = go.Figure()
        for index, _z in enumerate(zs):
            fig.add_trace(go.Scatter(
                x=[
                    df[x].min(),
                    df[x].max()
                ],
                y=np.full(2, len(zs)-index - overlap),
                # mode='lines',
                line_color='white'
            ))

            fig.add_trace(go.Scatter(
                x=array_dict[f'x_{_z}'],
                y=array_dict[f'y_{_z}'] + (len(zs)-index) + dist,
                fill='tonextx',
                name=f'{_z}'
            ))

            # Add the label for this z
            fig.add_annotation(
                x=-5,
                y=len(zs)-index,
                text=f'{_z}',
                showarrow=False,
                yshift=10
            )

        fig.update_layout(
            showlegend=False,
            xaxis_title=x,
            yaxis_title=y,
            # These aren't useful, since they're not on the correct scale
            yaxis_showticklabels=False,
            **kwargs
        )

        return fig
