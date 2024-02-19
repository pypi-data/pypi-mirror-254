import os
import unittest
import matplotlib.pyplot as plt
from unittest.mock import Mock, MagicMock
import numpy as np

try:
    import pltfront.plot as plotting
except:
    # This allows running the test within the tests folder
    import sys
    sys.path.append('../pltfront/')
    import plot as plotting


class TestPlot(unittest.TestCase):

    def setUp(self):
        # Initialize x, y
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 4, 6, 8, 10]
        self.y2 = [1, 3, 5, 7, 9]
        # Output directory
        out = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(out, exist_ok=True)
        self.out = out

        # Close any other open plots
        plt.close()

    # Plot a simple line plot with default parameters
    def test_simple_line_plot_default(self):
        plot = plotting.Plot()

        fig, ax = plot.plot(self.x, self.y, label='label')

        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsNotNone(ax.lines)
        self.assertEqual(len(ax.lines), 1)

    # Plot multiple lines on the same plot
    def test_multiple_lines_same_plot(self):
        plot = plotting.Plot()

        fig, ax = plot.plot([self.x, self.x], [self.y, self.y2], label=[None, None])

        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertEqual(len(ax.lines), 1)

    # Plot with empty x and y data
    def test_plot_with_empty_data(self):
        # Create an instance of the Plot class
        plot = plotting.Plot()

        # Call the plot method with empty x and y data and an empty label list
        fig, ax = plot.plot([], [], label=[])

        # Assert that the returned figure and axes are not None
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)

    # Save a plot to a file
    def test_save_plot_to_file(self):
        plot = plotting.Plot(out=self.out)

        fig, ax = plot.plot(self.x, self.y, save=True, label=['data'])

        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertTrue(os.path.exists(os.path.join(self.out, 'plot.eps')))

    # Plot with a non-existent stylesheet
    def test_nonexistent_stylesheet(self):
        stylesheet = "nonexistent.mplstyle"
        plot = plotting.Plot(out=self.out, stylesheet=stylesheet)

        # Check that the 'style' key is not in plt.rcParams
        self.assertNotIn('style', plt.rcParams)
        # Check that the plot extension is set to '.eps'
        self.assertEqual(plot.plot_extension, '.eps')

    # Plot with a custom skip value
    def test_plot_with_custom_skip_value(self):
        skip = 2
        plot = plotting.Plot()

        fig, ax = plot.plot(self.x, self.y, skip=skip)

        # Check that the skip value is applied correctly
        self.assertEqual(ax.lines[0].get_xdata().tolist(), self.x[::skip])
        self.assertEqual(ax.lines[0].get_ydata().tolist(), self.y[::skip])

    # Plot with specific plot kwargs
    def test_plot_with_specific_kwargs(self):
        # Create test data
        plot_kwargs = {'color': 'red', 'linestyle': '--'}

        # Create an instance of the Plot class
        plot = plotting.Plot()

        # Call the plot() method with specific plot kwargs
        fig, ax = plot.plot(self.x, self.y, plot_kwargs=plot_kwargs)

        # Check if the plot was created with the specific plot kwargs
        line = ax.lines[0]
        self.assertEqual(line.get_color(), 'red')
        self.assertEqual(line.get_linestyle(), '--')

    # Plot with custom error bar settings
    def test_custom_error_bar_settings(self):
        xerr = [0.1, 0.2, 0.3, 0.4, 0.5]
        yerr = [0.2, 0.4, 0.6, 0.8, 1.0]
        kwargs = {'elinewidth': '12', 'ecolor': 'red'}

        plot = plotting.Plot()
        fig, ax = plot.plot(self.x, self.y, xerr=xerr, yerr=yerr, error_kwargs=kwargs)

        # Check that the plot has the correct additional kwargs
        self.assertEqual(ax.collections[1].get_linewidth()[0], '12')
        self.assertListEqual(ax.collections[1].get_edgecolor()[0].tolist(), [1., 0., 0., 1.])

    # Create a custom style sheet and check if it's used correctly in the plot
    def test_custom_style_sheet(self):
        """
        Test that a custom style sheet is used correctly in the plot
        """
        # Create a mock stylesheet file
        mock_stylesheet = os.path.join(self.out, 'mock_stylesheet.mplstyle')
        with open(mock_stylesheet, 'w') as f:
            f.write('grid.linestyle : dashed')

        # Create a mock Plot object with the custom style sheet
        plot = plotting.Plot(stylesheet=mock_stylesheet)

        # Call the plot method with some data
        plot.plot(self.x, self.y)

        # Check that the grid linestyle is set to 'dashed'
        self.assertEqual(plt.rcParams['grid.linestyle'], 'dashed')

        # Delete the mock stylesheet file
        os.remove(mock_stylesheet)

    def test_set_axis_limits(self):
        plot = plotting.Plot()
        kind = 'line'
        xlab = 'X-axis'
        ylab = 'Y-axis'
        xlim = (0, 6)
        ylim = (0, 12)

        fig, ax = plot.plot(self.x, self.y, xlabel=xlab, ylabel=ylab, xlim=xlim, ylim=ylim)

        self.assertEqual(ax.get_xlabel(), xlab)
        self.assertEqual(ax.get_ylabel(), ylab)
        self.assertEqual(ax.get_xlim(), xlim)
        self.assertEqual(ax.get_ylim(), ylim)

    def test_set_axes_kwarg(self):
        plot = plotting.Plot()
        fig, ax = plot.plot(self.x, self.y, frame_on=False)

        self.assertEqual(ax.get_frame_on(), False)

    def test_update_with_new_properties(self):
        # Initialize the Plot class object with an output directory
        plot = plotting.Plot(out=self.out)

        # Create a plot using the plot method
        fig, ax = plot.plot(self.x, self.y)

        # Update the existing plot with new properties using the update method
        updated_fig, updated_ax = plot.update(title='Updated Plot', save=True)

        # Assert that the updated plot has the new properties
        self.assertEqual(updated_ax.get_title(), 'Updated Plot')
        self.assertTrue(os.path.exists(self.out + '/plot.eps'))

    def test_update_with_no_axes_or_figure(self):
        # Initialize the Plot class object
        plot = plotting.Plot()

        # Try to update the plot with no axes or figure provided
        with self.assertRaises(AttributeError):
            plot.update()

    # Mismatch between last axes and figure raises AssertionError
    def test_mismatch_axes_figure(self):
        # Initialize the Plot class object
        plot = plotting.Plot()

        # Create a plot using the plot method
        fig1, ax1 = plot.plot(self.x, self.y)

        # Create another plot
        fig2, ax2 = plt.subplots()
        ax2.plot([1, 2, 4], [4, 5, 6])

        # Assert that calling update with mismatched axes and figure raises an AssertionError
        with self.assertRaises(AssertionError):
            plot.update(fig=fig2)

    # Loading a pickled plot object
    def test_load_pickled_plot_object(self):
        # Create a Plot object
        plot = plotting.Plot(out=self.out)

        # Plot the data and save the figure
        fig, ax = plot.plot(self.x, self.y, kind='line', label='data', show=False)

        # Store the plot as a pickled object
        plot.store('fig_object')

        # Load the pickled plot object
        load_fig, load_ax = plot.load('fig_object')

        # Check if the loaded plot objects are the same as the original plot objects
        self.assertEqual(load_fig, plot.last_fig)
        self.assertEqual(load_ax, plot.last_ax)

    def test_store_and_load_plot_compare_properties(self):
        # Create a Plot object
        plot = plotting.Plot(out=self.out)

        # Plot the data
        fig, ax = plot.plot(self.x, self.y)

        # Store the plot
        plot.store('fig')

        # Load the stored plot
        plot.load('fig')
        loaded_fig = plot.last_fig 
        loaded_ax = plot.last_ax

        # Check if the loaded plot matches the original plot
        self.assertEqual(fig.get_dpi(), loaded_fig.get_dpi())
        self.assertEqual(fig.get_facecolor(), loaded_fig.get_facecolor())
        self.assertEqual(fig.get_edgecolor(), loaded_fig.get_edgecolor())
        self.assertEqual(fig.get_frameon(), loaded_fig.get_frameon())
        self.assertEqual(fig.get_tight_layout(), loaded_fig.get_tight_layout())
        self.assertEqual(fig.get_label(), loaded_fig.get_label())
        self.assertCountEqual(fig.get_size_inches(), loaded_fig.get_size_inches())
        self.assertEqual(fig.get_gid(), loaded_fig.get_gid())
        self.assertEqual(fig.get_zorder(), loaded_fig.get_zorder())

    def tearDown(self):
        # Remove output directory
        import shutil
        shutil.rmtree(self.out)

'''
class Test(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(0., 1., 100)
        self.y = np.exp(self.x)
        self.xs = [self.x for _ in range(2)]
        self.ys = [np.exp(self.x), np.exp(2*self.x)]

        # Output directory handling
        out = os.path.join(os.path.dirname(__file__), 'out')
        if not os.path.exists(out): 
            os.makedirs(out)
        self.out = out

    @mock.patch(f"{__name__}.plot.plt.Axes")
    def test_simple_plot(self, mock_plt):
        """Test every kind of simple plot available """

        plotting = plot.Plot()
        # Configure mock object to work with subplots (they get unpacked into
        # fig, ax
        mock_plt.subplots.return_value = (mock.MagicMock(), mock.MagicMock())
        # Test every kind of plot iteratively
        _mock_plt_db = {'scatter': mock_plt.scatter, 'line': mock_plt.plot,
                        'semilogx': mock_plt.semilogx, 'semilogy': mock_plt.semilogy, 'loglog': mock_plt.loglog}
        for key, value in _mock_plt_db.items():
            plotting.plot(self.x, self.y, mock_plt, kind=key)
            value.assert_called_once()

    @mock.patch(f"{__name__}.plot.plt")
    def test_multiple_plot(self, mock_plt):
        """Test every kind of multiple superimposed plot available"""

        plotting = plot.Plot()
        # Configure mock object to work with subplots (they get unpacked into
        # fig, ax
        mock_plt.subplots.return_value = (mock.MagicMock(), mock.MagicMock())
        # Test every kind of plot iteratively
        _mock_plt_db = {'scatter': mock_plt.scatter, 'line': mock_plt.plot,
                        'semilogx': mock_plt.semilogx, 'semilogy': mock_plt.semilogy, 'loglog': mock_plt.loglog}
        for key, value in _mock_plt_db.items():
            plotting.plot(self.xs, self.ys, mock_plt, kind=key)
            value.assert_called()

    def test_save(self):
        """Test plot saving to file"""
        plotting = plot.Plot()
        plotting.out = self.out

        plotting.plot(self.x, self.y, filename='plot', save=True)
        assert os.path.exists(os.path.join(plotting.out, 'plot.eps'))

        # Try another extension
        plotting.plot_extension = '.png'
        plotting.plot(self.x, self.y, filename='plot', save=True)
        assert os.path.exists(os.path.join(plotting.out, 'plot.png'))

    def tearDown(self):
        # Remove output directory
        import shutil
        shutil.rmtree(self.out)
'''
