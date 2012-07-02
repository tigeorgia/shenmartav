from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class IncomeDeclarationApp (CMSApp):
    name = _('Income Declaration App')
    urls = ['incomedeclaration.urls']
apphook_pool.register(IncomeDeclarationApp)
