"""
Views incomedeclaration
"""
__docformat__ = 'epytext en'

from django.views.generic import DetailView, ListView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

from .models import IncomeDeclaration



class List (ListView):
    model = IncomeDeclaration
    template_name = 'incomedeclaration/list.html'
    queryset = IncomeDeclaration.objects.all()
    paginate_by = 30



class Detail (DetailView):
    context_object_name = 'obj'
    model = IncomeDeclaration
    template_name = 'incomedeclaration/detail.html'
    slug_field = 'slug'


    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        set_language_changer(self.request, context['obj'].get_absolute_url)
        return context
