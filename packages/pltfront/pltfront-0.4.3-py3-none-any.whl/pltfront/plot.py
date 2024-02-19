import os
import inspect as ins
import pickle
import warnings

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

try:
    from factory import PlotFactory
except:
    import sys
    sys.path.append('../pltfront/')
    from pltfront.factory import PlotFactory


# Utilities
def _data_conv(x, verbose=False):
    """Convert dicts or generic size lists to ndarrays, preserving keys"""

    keys = None
    if isinstance(x, dict):
        xd = np.asarray(list(x.values()))
        keys = np.asarray(list(x.keys()))
    # List or np.array: check if it's 1D or ND
    elif (isinstance(x, list) or isinstance(x, np.ndarray)):
        # If it's 1D, convert to ndarray with size (1, n_elements)
        if np.ndim(x) == 1:
            xd = np.array(x, ndmin=2)
        else:
            xd = np.array(x)
    else:
        raise TypeError(f'x is {type(x)}, not a list or dict')

    if verbose:
        print('xd', np.shape(xd), len(xd), np.ndim(xd))
    return xd, keys


def _kwarg_conv(kwarg, length=None, verbose=False):
    """From kwarg dictionary or list of dicts, to list of dicts of proper length"""
    if isinstance(kwarg, list):
        if all(isinstance(v, dict) for v in kwarg):
            lst = np.array(kwarg, ndmin=1)
    elif isinstance(kwarg, dict):
        lst = np.array(kwarg, ndmin=1)
    else:
        warnings.warn(f'kwarg is a {type(kwarg)}, not a dict.', RuntimeWarning)
        lst = np.array([{}])

    if length is not None:
        if np.shape(lst)[0] < length:
            # Pad the list if it's shorter than expected
            while np.shape(lst)[0] < length:
                lst = np.append(lst, {})
    if verbose:
        print(type(lst), lst)
    return lst


def _kwarg_inject(kwarg, to_add, name, pad=True):
    """Inject new kwarg in kwarg list of dicts"""
    # Sanity checks
    assert isinstance(
        kwarg, np.ndarray), f'kwarg list is not a list: got {type(kwarg)}'
    assert (isinstance(to_add, np.ndarray) or isinstance(to_add, list)
            ), f'items to add is not a list: got {type(to_add)}'

    # Pad list if shorter
    if pad:
        if len(kwarg) > len(to_add):
            delta = len(kwarg) - len(to_add)
            try:
                to_add.extend([None for _ in range(delta)])
            except AttributeError:
                to_add = np.concatenate((to_add, np.asarray([None for _ in range(delta)])))

    # Inject kwargs
    for idx, item in enumerate(to_add):
        try:
            kwarg[idx][name] = item
        except IndexError:
            # this handles len(to_add) > len(kwarg)
            break
    return kwarg

# Plot


class Plot:
    def __init__(self, out=None, stylesheet=None):
        # Handle output directory
        self.out = out
        """Main output directory."""

        if out is not None:
            # Create output directory
            os.makedirs(self.out, exist_ok=True)

            # Generate object storing directory
            self.out_store = os.path.join(out, 'pkl')
            """Pickled object output directory."""
            os.makedirs(self.out_store, exist_ok=True)

            assert os.path.exists(self.out), f'{out} is not a directory'
            assert os.path.exists(self.out_store), f'{out} is not a directory'

        # Handle stylesheet directory
        self.stylesheet = stylesheet
        if stylesheet is not None:
            if os.path.isfile(stylesheet):
                _, ext = os.path.splitext(stylesheet)
                assert ext == '.mplstyle', f"wrong matplotlib style sheet extension {ext}"

        # Extensions
        self.plot_extension = '.eps'
        """General image extension."""
        self.store_extension = '.pkl'
        """Pickled fig, ax extension."""

        # Axes and figure
        self.inp_ax = None
        """Current axes, used for input"""
        self.inp_fig = None
        """Current figure, used for input"""
        self.last_ax = None
        """Last axes, saved regardless of `store` parameter"""
        self.last_fig = None
        """Last figure, saved regardless of `store` parameter"""
        self.all_axes = []
        """Stored axes"""
        self.all_figure = []
        """Stored figure"""

    def _no_stylesheet(self, fig, ax, grid=False, grid_line='dashed', number_minor_x=None, number_minor_y=None, legend=False, legend_frame=False, size=[5, 5]):
        """
        Set style options for a plot when no stylesheet is provided. All keyword arguments are fetched from `plot`.

        Parameters
        ----------
        grid:           bool, optional
                        whether to show grid lines on the plot. Default is False.
        grid_line:      str, optional
                        linestyle for the grid lines. Default is 'dashed'.
        number_minor_x: int, optional
                        number of minor ticks on the x-axis. Default is None.
        number_minor_y: int, optional
                        number of minor ticks on the y-axis. Default is None.
        legend:         bool, optional
                        whether to show a legend on the plot. Default is False.
        legend_frame:   bool, optional
                        whether to show a frame around the legend. Default is False.
        size:           list, optional
                        size of the figure in inches. Default is [5, 5].
        """

        # Size
        fig.set_size_inches(size[0], size[1])

        # Ticks
        ax.minorticks_on()
        ax.tick_params(which='both', direction='in', top=True, right=True)
        ax.tick_params(which='major', size=8)
        ax.tick_params(which='minor', size=5)
        if number_minor_x:
            ax.xaxis.set_minor_locator(tic.AutoMinorLocator(number_minor_x))
        if number_minor_y:
            ax.yaxis.set_minor_locator(tic.AutoMinorLocator(number_minor_y))

        # Set grid
        if grid:
            ax.grid(visible=grid, linestyle=grid_line)

        # Legend
        if legend:
            ax.legend(frameon=legend_frame)

    def save(self, filename, bbox_inches, fig=None):
        """
        Save specified plot.
        """

        if fig is None and self.last_fig is not None:
            fig = self.last_fig
        elif self.last_fig is None:
            raise AttributeError(
                'no figure specified, or no existing figure to update.')

        assert os.path.exists(self.out), 'output directory does not exist or has not been specified.'

        fig.savefig(os.path.join(self.out, filename +
                    self.plot_extension), bbox_inches=bbox_inches)

    def show(self, fig=None):
        """Show figure not on top of stack by creating a dummy"""

        if fig is None and self.last_fig is not None:
            fig = self.last_fig
        elif self.last_fig is None:
            raise AttributeError(
                'no figure specified, or no existing figure to update.')

        dummy = plt.figure(figsize=fig.get_size_inches())
        new_manager = dummy.canvas.manager
        new_manager.canvas.figure = fig
        fig.set_canvas(new_manager.canvas)
        plt.show()
        plt.close(dummy)

    def store(self, fig_name, fig=None):
        """Pickle figure"""

        # Get axes and figs
        if fig is None and self.last_fig is not None:
            fig = self.last_fig
        elif self.last_fig is None:
            raise AttributeError(
                'no figure specified, or no existing figure to store.')

        # Store objects
        print(fig)
        with open(os.path.join(self.out_store, fig_name+self.store_extension), 'wb') as f:
            pickle.dump(fig, f)

    def load(self, fig_name, clear=False):
        """Unpickle figure and axes"""

        warnings.warn('CRITICAL: only load files you trust. Malicious code can be executed - no checks are performed on loaded data!', RuntimeWarning)

        fig_obj = os.path.join(self.out_store, fig_name+self.store_extension)
        with open(fig_obj, 'rb') as f:
            self.last_fig = pickle.load(f)

        self.last_ax = self.last_fig.axes

        if clear:
            os.remove(fig_obj)

        return self.last_fig, self.last_ax

    def plot(self, x, y, kind='line', label=None, skip=None, xerr=None, yerr=None, skiperr=1, bbox_inches='tight', filename='plot', save=False, close=True, show=False, store=False, plot_kwargs={}, error_kwargs={}, **kwargs):
        """
        Generic plot routine. Other keyword arguments are passed to
        `_nostylesheet` and Axes.set().

        Parameters
        ----------
        x:              array-like
                        x-axis data for the plot.
        y:              array-like
                        y-axis data for the plot.
        kind:           str, optional
                        type of plot to create (e.g., line, scatter).
        label:          str, optional
                        legend label for each plot.
        skip:           int, optional
                        number of data points to skip when plotting.
        xerr:           array-like, optional
                        error bars for the x-axis data.
        yerr:           array-like, optional
                        error bars for the y-axis data.
        skiperr:        int, optional
                        number of error bars to skip.
        title:          str, optional
                        title of the plot.
        bbox_inches:    str, optional
                        bounding box for the plot.
        filename:       str, optional
                        filename to save the plot as.
        save:           bool, optional
                        whether to save the plot.
        close:          bool, optional
                        whether to close the plot after displaying it.
        show:           bool, optional
                        whether to display the plot.
        **plot_kwargs:  dict, optional
                        additional keyword arguments for plot customization.
        **axes_kwargs:  dict, optional
                        additional keyword arguments for axes customization.
        **error_kwargs: dict, optional
                        additional keyword arguments for errorbar customization.

        Returns
        -------
        fig, ax:        tuple
                        contains the figure object and the axes object of the plot.
        """

        # 1. Core plot
        # If stylesheet is set, use it asap
        if self.stylesheet is not None:
            plt.style.use(self.stylesheet)

        # Define figure
        if self.inp_fig is None and self.inp_ax is None:
            fig, ax = plt.subplots(tight_layout={'pad': 0})

        # kwarg handling
        keep_style = list(ins.signature(self._no_stylesheet).parameters.keys())
        keep_axset = list(ins.signature(ax.set).parameters.keys())
        kwargs_style = {k: kwargs[k] for k in keep_style if k in kwargs.keys()}
        kwargs_axset = {k: kwargs[k] for k in keep_axset if k in kwargs.keys()}
        kwargs = {k: v for k, v in kwargs.items(
        ) if k not in kwargs_style | kwargs_axset}

        # Check dimensionality
        # Convert x, y and extract plot kind from dict
        xs, kinds = _data_conv(x)
        ys, _ = _data_conv(y)

        # If x isn't a dict, fetch user-specified kinds
        if kinds is None:
            kinds = np.array(kind, ndmin=1)

        # Sanity check
        # Checks on x and y
        ndim = np.shape(xs)
        assert ndim == np.shape(
            ys), f'x and y have mismatching shapes, {ndim} and {np.shape(ys)}'

        # Check xs and kinds have same dimension
        if ndim[0] > np.shape(kinds)[0]:
            warnings.warn(
                f'x and kind have mismatching first dims, ({ndim[0]}) and ({np.shape(kinds)[0]}). Remaining kinds set to scatter.', RuntimeWarning)
            while np.shape(kinds)[0] < ndim[0]:
                kinds = np.append(kinds, 'scatter')

        # Convert label to array
        labels = np.array(label, ndmin=1)

        # Check xs and labels have same dimension
        if ndim[0] > np.shape(labels)[0]:
            warnings.warn(
                f'x and labels have mismatching first dims, ({ndim[0]}) and ({np.shape(labels)[0]}). Labels set to `None`.', RuntimeWarning)
            labels = [None for _ in range(ndim[0])]

        # Extra user specified kwarg cleanup
        plot_kwargs = _kwarg_conv(plot_kwargs, length=ndim[0])
        plot_kwargs = _kwarg_inject(plot_kwargs, labels, 'label', pad=True)
        error_kwargs = _kwarg_conv(error_kwargs, length=ndim[0])

        # Instantiate plots
        plots = [PlotFactory(xi[::skip], yi[::skip], xerr=xerr, yerr=yerr, kind=kindi, ax=ax)
                 for xi, yi, kindi in zip(xs, ys, kinds)]

        # Do the plots
        for i in range(ndim[0]):
            ax = plots[i].plot(plot_kwargs[i], error_kwargs[i])

        # 2. Data features
        # Axis labels, limits and all optional args
        ax.set(**kwargs_axset)

        # 3. Style features
        # Don't show legend if no labels are available
        if all(item is None for item in labels):
            kwargs_style['legend'] = False

        if self.stylesheet is None:
            self._no_stylesheet(fig, ax, **kwargs_style)

        # 4. Show, save and close
        # Store plot object
        self.last_fig = fig
        self.last_ax = ax
        if store:
            self.all_figure.append(fig)
            self.all_axes.append(ax)

        # Save plot
        if save:
            self.save(filename, bbox_inches, fig=fig)

        # Show plot
        if show:
            plt.show()
        if close:
            plt.close(fig)

        return fig, ax

    def update(self, fig=None, ax=None, bbox_inches='tight', filename='plot', save=False, show=True, close=False, **kwargs):
        """
        Update existing plot, allowing change of existing plot properties.
        Only axes and figure data can be modified.
        Note:   if figure and axes are mismatched, there is no way to check.
                Specified figure is going to be shown or saved, while passed
                axes are getting ignored.

        Parameters
        ----------
        **error_kwargs: dict, optional
                        additional keyword arguments for errorbar customization.
        fig:            optional
                        figure object of the plot to be updated.
        ax:             optional
                        axes object of the plot to be updated.
        bbox_inches:    optional
                        bounding box for the plot when saving.
        filename:       optional, str
                        The filename to save the plot as.
        save:           optional, bool
                        Whether to save the plot.
        show:           optional, bool
                        Whether to display the plot.
        close:          optional, bool
                        Whether to close the plot after displaying it.
        **kwargs:       optional
                        Additional keyword arguments passed to `Axes.set()`.

        Returns
        -------
        fig, ax:        tuple
                        contains the figure object and the axes object of the plot.

        """
        # Get axes and figs
        if fig is None and self.last_fig is not None:
            fig = self.last_fig
        elif self.last_fig is None:
            raise AttributeError(
                'no figure specified, or no existing figure to update.')
        if ax is None and self.last_ax is not None:
            assert fig == self.last_fig, 'Mismatch between last axes and figure.'
            ax = self.last_ax
        elif self.last_ax is None:
            raise AttributeError(
                'no axes specified, or no existing axes to update.')

        keep_axset = list(ins.signature(ax.set).parameters.keys())
        kwargs_axset = {k: kwargs[k] for k in keep_axset if k in kwargs.keys()}

        # Set properties
        ax.set(**kwargs_axset)

        # Save plot
        if save:
            self.save(filename, bbox_inches, fig=fig)

        # Show plot
        if show:
            self.show(fig)
        if close:
            plt.close(fig)

        return fig, ax
