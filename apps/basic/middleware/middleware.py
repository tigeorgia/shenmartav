from django.http import HttpResponse
from django.conf import settings

class MaintenanceMiddleware(object):

    def process_request(self, request):
        if not settings.MAINTENANCE or request.META.get('REMOTE_ADDR') in settings.MAINTENANCE_EXCLUDED_IPS:
            pass
        else:
            return HttpResponse(
                content='<html><head></head><body><p style="text-align:center;font-size: 25px;top: 73;">Under construction</p></body></html>',
                status="503")
