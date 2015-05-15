#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################
# update site's domain and reset admin password
###########################################################

import os, sys
sys.path.append(os.path.curdir)
sys.path.append(os.path.join(os.path.curdir, '..'))
sys.path.append('/home/tigeorgia/shenmartav')
sys.path.append('/home/tigeorgia/shenmartav/shenmartav')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shenmartav.settings'

import settings
settings.HAYSTACK_ENABLE_REGISTRATIONS = False

from django.contrib.sites.models import Site
site = Site.objects.get_current()
site.domain = 'shenmartav.ge'
site.save()


from django.contrib.auth.models import User
admin = User.objects.get(pk=1)
admin.set_password('admin')
admin.save()
