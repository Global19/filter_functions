# -*- coding: utf-8 -*-
# =============================================================================
#     filter_functions
#     Copyright (C) 2019 Quantum Technology Group, RWTH Aachen University
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#     Contact email: tobias.hangleiter@rwth-aachen.de
# =============================================================================
"""Package for efficient calculation of generalized filter functions"""

from . import analytic, basis, numeric, plotting, pulse_sequence, util
from .basis import Basis
from .numeric import (infidelity, liouville_representation,
                      error_transfer_matrix)
from .plotting import (plot_bloch_vector_evolution, plot_filter_function,
                       plot_pulse_correlation_filter_function,
                       plot_pulse_train, plot_error_transfer_matrix)
from .pulse_sequence import (PulseSequence, concatenate, concatenate_periodic,
                             extend, remap)

__all__ = ['PulseSequence', 'concatenate', 'extend', 'Basis', 'numeric',
           'plot_filter_function', 'plot_bloch_vector_evolution',
           'plot_pulse_train', 'util', 'plotting', 'analytic', 'basis',
           'infidelity', 'plot_pulse_correlation_filter_function',
           'concatenate_periodic', 'pulse_sequence', 'remap',
           'error_transfer_matrix', 'plot_error_transfer_matrix',
           'liouville_representation']

__version__ = '0.1.0'
__license__ = 'GNU GPLv3+'
__author__ = 'Quantum Technology Group, RWTH Aachen University'
