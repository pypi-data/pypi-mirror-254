# pltfront - a simple matplotlib frontend

**pltfront** is a bare-bones Python plotting package, which provides an easy interface for `matplotlib` and removes some complexity from repetitive plotting tasks.

## Quick start

Let's plot the exponential function in [0, 1]
```python
from pltfront.plot import Plot
import numpy as np

# Generate the data set
x = np.linspace(0., 1.)
y = np.exp(x)

# Plot
label = "$e^x$"

plotting = Plot()
plotting.plot(x, y, kind='line', label=label, legend=True, title=r'$f(x)=e^x$', show=True)
```

For multiple superimposed plots, a list of lists is all it takes
```python
xs = [x for i in range(2)]
ys = [np.exp(x), np.exp(2*x)]

labels = ["$e^x$", "$e^{2x}$"]
kinds = ['line', 'scatter']

_ = plotting.plot(xs, ys, label=labels, kind=kinds, legend=True, show=True)
```

## Features
- Simple interface for `matplotlib` plotting functions
- User-specified plotting functions can be used (as long as they are callable!)
- Multiple plots can be superimposed

## Requirements
- `matplotlib >= 3.8.0`
- `numpy >= 1.26.0`

## Documentation
Check out the [tutorial](https://codutils.frama.io/pltfront/tutorial) for more examples and the [public API](https://codutils.frama.io/pltfront/api/pltfront) for more details.

## Contributions
Contributions are welcome! Please follow the [guidelines](https://framagit.org/codutils/pltfront/-/blob/master/CONTRIBUTING.md) available in the repository.

## Installation
From the Python Package Index
```
pip install pltfront
```

From the code repository
```
git clone https://framagit.org/codutils/pltfront.git
cd pltfront
make install
```

## Author
[Iacopo Ricci](https://iricci.frama.io)
