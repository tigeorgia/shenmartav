# vim: set fileencoding=utf-8
"""
Pie chart for representative

Depends on matplotlib
"""
__docformat__ = 'epytext en'

import os
from pylab import *

from django.utils.translation import ugettext as _
from settings import PIECHART_DIR



class PieChart (object):
    """A pie chart to save to disk."""
    def __init__(self):
        self.total = 0

        # would be nice to get these from a stylesheet
        self.figsize = (1.7, 1.7) # inches
        self.colors = ['#d44847', '#e08c8c'];
        rcParams['text.color'] = '#ffffff'
        rcParams['font.size'] = 10


    def _inside_label (self, pct):
        val = int(pct * self.total / 100.0)
        return '{v:d}'.format(v=val)


    def save (self, filename, fracs):
        """Save SVG pie chart to disk.

        @param filename: filename to save to, without directory and '.svg'
        @type filename: str
        @param fracs: fractions of the pie
        @type fracs: [ int, int ]
        """
        self.total = sum(fracs)
        f = figure(figsize=self.figsize, frameon=False)

        patches, texts, autotexts = pie(fracs,
            colors=self.colors,
            autopct=self._inside_label)
        for p in patches: # remove border ('stroke' in svg)
            p.set_linewidth(0)

        if not os.path.exists(PIECHART_DIR):
            os.mkdir(PIECHART_DIR)
        savefig(os.path.join(PIECHART_DIR, filename + '.svg'),
            bbox_inches=0, transparent=True)

        close(f)
