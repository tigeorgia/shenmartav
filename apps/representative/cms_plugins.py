# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import RandomRepresentative, ParliamentManager
from .views import UnitParliament


class RepresentativeListPlugin (CMSPluginBase):
    model = CMSPlugin
    name = _('Representative List Plugin')
    render_template = 'representative/unit_as_3rows.html'

    #TODO: Again, kinda hacky, convert view to plugin?
    def render(self, context, instance, placeholder):
        unit = UnitParliament()
        context['members'] = unit._get_members()
        return context
plugin_pool.register_plugin(RepresentativeListPlugin)

class AttendanceStatsPlugin (CMSPluginBase):
    model = CMSPlugin
    name = _('Best / Worst attendance plugin')
    render_template = 'representative/best-worst-attendance.html'

    def render(self, context, instance, placeholder):
       mgr = ParliamentManager()
       mps = mgr.get_query_set().filter(attendance__total__gt=0)
       bestMp = mps.order_by('-attendance__percentage_attended','?')[0] 
       worstMp = mps.order_by('attendance__percentage_attended','?')[0]
       context['bestmp'] = bestMp
       context['worstmp'] = worstMp
       context['bestattend'] = bestMp.attendance.get()
       context['worstattend'] = worstMp.attendance.get()
       return context
plugin_pool.register_plugin(AttendanceStatsPlugin)

class IncomeStatsPlugin (CMSPluginBase):
    model = CMSPlugin
    name = _('Highest / Lowest income plugin')
    render_template = 'representative/high-low-income.html'

    def render(self, context, instance, placeholder):
        mgr = ParliamentManager()
        mps = sorted(mgr.get_query_set(), key=lambda r: r.income["total"])
        context['highmp'] = mps[-1]
        context['lowmp'] = mps[0]
        return context
plugin_pool.register_plugin(IncomeStatsPlugin)
