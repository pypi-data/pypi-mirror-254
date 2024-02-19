import numpy as np
import matplotlib.pyplot as plt


class PlotFactory:
    """
    Plot object factory
    """

    def __init__(self, x, y, xerr=None, yerr=None, kind='line', ax=None):
        # Initialize vars
        self.x = x
        self.y = y
        self.x_err = xerr
        self.y_err = yerr

        # Axes handling
        if ax is None:
            self.ax = plt.gca()
        else:
            self.ax = ax

        # Available plot functions
        self._plots_db = {'scatter': self.ax.scatter, 'line': self.ax.plot,
                          'semilogx': self.ax.semilogx, 'semilogy': self.ax.semilogy, 'loglog': self.ax.loglog}
        self.available_plots = list(self._plots_db.keys())

        # Plot kind handling
        # Deprecation warning
        if kind in ['semilogx', 'semilogy', 'loglog']:
            raise DeprecationWarning(f'{kind} is not recommended and will be deprecated soon. Use Plot.plot(..., xscale=..., yscale=...)')
        # Strategy
        if kind in self._plots_db.keys():
            self._plot = self._plots_db[kind]
        elif kind is None:
            self._plot = self._plots_db['scatter']
        else:
            assert hasattr(
                kind, '__call__'), f'kind must be in{list(self._plots_db.keys())} or callable'
            self._plot = kind

    def plot(self, plot_kwargs={}, error_kwargs={}):
        """Plot function creation"""

        # Plot
        self._plot(self.x, self.y, **plot_kwargs)

        # Errorbars
        if (np.any(self.x_err) is not None or np.any(self.y_err) is not None):
            self.ax.errorbar(self.x, self.y, yerr=self.y_err,
                             xerr=self.x_err, **error_kwargs)  # errorevery=skiperr, markevery=skiperr, capsize=2)

        return self.ax

    def plot3d(self, *args, **kwargs):
        """3D plot function creation"""
        raise NotImplementedError("WIP")
        return self._plot3d(self.x, self.y, self.z, **kwargs)
