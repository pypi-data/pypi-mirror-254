import numpy as np
from collections import namedtuple
from scipy.stats import chi2

_chist = namedtuple('plottergeist_histogram',
                    ['bins', 'counts', 'yerr', 'xerr', 'norm', 'edges'])

def get_errors_poisson(data, a=0.318):
  """
  Uses chi-squared info to get the poisson interval.
  """
  low, high = chi2.ppf(a/2, 2*data) / 2, chi2.ppf(1-a/2, 2*data + 2) / 2
  return np.array(data-low), np.array(high-data)


def get_errors_sW2(x, weights=None, range=None, bins=60):
  if weights is not None:
    values = np.histogram(x, bins, range, weights=weights*weights)[0]
  else:
    values = np.histogram(x, bins, range)[0]
  return np.sqrt(values)


def make_hist(data, bins=None, weights=None, center_of_mass=False, density=False,
         **kwargs):
  """
    Wrap around NumPy histogram. Saves integral ('norm'), center-of-mass bins
    ('cmbins'), edges ('edges'), errors on bins and counts ('xerr', 'yerr'), etc.
  """

  # Histogram data
  counts, edges = np.histogram(data, bins=bins, weights=weights, density=False,
                               **kwargs)
  cbins = 0.5 * (edges[1:] + edges[:-1])
  norm = np.sum(counts)*(cbins[1]-cbins[0])

  # Compute the mass-center of each bin
  if center_of_mass:
    for k in range(0,len(edges)-1):
      if counts[k] != 0:
        cbins[k] = np.median( data[(data>=edges[k]) & (data<=edges[k+1])] )

  # Compute yerr
  if weights is not None:
    y_errl, y_errh = get_errors_poisson(counts)
    y_errl = y_errl**2 + get_errors_sW2(data, weights=weights, bins=bins, **kwargs)**2
    y_errh = y_errh**2 + get_errors_sW2(data, weights=weights, bins=bins, **kwargs)**2
    y_errl = np.sqrt(y_errl)
    y_errh = np.sqrt(y_errh)
  else:
    y_errl, y_errh = get_errors_poisson(counts)

  x_errh = edges[1:] - cbins
  x_errl = cbins - edges[:-1]


  # Normalize if asked so
  if density:
    counts = counts/norm
    y_errl = y_errl/norm
    y_errh = y_errh/norm


  histogram = _chist(cbins, counts, [y_errl, y_errh], [x_errl, x_errh], norm, edges)

  return histogram
