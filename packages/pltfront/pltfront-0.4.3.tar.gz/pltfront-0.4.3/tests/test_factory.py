import unittest
import matplotlib.pyplot as plt
from unittest.mock import Mock, MagicMock

try:
    import pltfront.factory as pf
except:
    # This allows running the test within the tests folder
    import sys
    sys.path.append('../pltfront/')
    import factory as pf


class TestPlotFactory(unittest.TestCase):

    def setUp(self):
        # Initialize x, y
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 4, 6, 8, 10]
        # Close any other open plots
        plt.close()

    # Creating a PlotFactory object with x and y values should initialize the object with the given values.
    def test_initialize_with_x_and_y_values(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        plot_factory = pf.PlotFactory(self.x, self.y)

        self.assertEqual(plot_factory.x, self.x)
        self.assertEqual(plot_factory.y, self.y)

    # Creating a PlotFactory object with xerr and yerr values should initialize the object with the given error values.
    def test_initialize_with_xerr_and_yerr_values(self):
        x_err = [0.1, 0.2, 0.3, 0.4, 0.5]
        y_err = [0.2, 0.4, 0.6, 0.8, 1.0]

        plot_factory = pf.PlotFactory(self.x, self.y, xerr=x_err, yerr=y_err)

        self.assertEqual(plot_factory.x_err, x_err)
        self.assertEqual(plot_factory.y_err, y_err)

    # Creating a PlotFactory object with no x and y values should raise an error.
    def test_initialize_with_no_x_and_y_values_raises_error(self):
        with self.assertRaises(TypeError):
            pf.PlotFactory()

    # Creating a PlotFactory object with xerr and yerr values of different lengths should not raise an error.
    def test_initialize_with_different_lengths_of_xerr_and_yerr_values_does_not_raise_error(self):
        x_err = [0.1, 0.2, 0.3, 0.4]
        y_err = [0.2, 0.4, 0.6, 0.8, 1.0]

        try:
            pf.PlotFactory(self.x, self.y[0:3], xerr=x_err, yerr=y_err)
        except ValueError:
            self.fail("ValueError raised when initializing PlotFactory with different lengths of xerr and yerr values.")

    # Calling the plot method with no x and y error values should plot the x and y values without error bars.
    def test_plot_method_plots_x_and_y_values_without_error_bars(self):
        plot_factory = pf.PlotFactory(self.x, self.y)
        mock_ax = MagicMock()
        plot_factory.ax = mock_ax

        plot_factory.plot()

        mock_ax.errorbar.assert_not_called()

    # Creating a PlotFactory object with a label should label the plot with the given label.
    def test_initialize_with_label(self):
        plot_kwargs = {'label': 'data'}
        plot_factory = pf.PlotFactory(self.x, self.y)

        plot_factory.plot(plot_kwargs=plot_kwargs)

        self.assertEqual(plot_factory.ax.get_legend_handles_labels()[1], ['data'])

    # Calling the plot method with a callable kind kwarg should generate a plot using said callable, e.g. plt.plot
    def test_plot_with_callable_kind_kwarg(self):
        kind = plt.plot

        plot_factory = pf.PlotFactory(self.x, self.y, kind=kind)
        plot_factory.plot()

        self.assertEqual(plot_factory._plot, kind)
        self.assertEqual(len(plot_factory.ax.lines), 1)
